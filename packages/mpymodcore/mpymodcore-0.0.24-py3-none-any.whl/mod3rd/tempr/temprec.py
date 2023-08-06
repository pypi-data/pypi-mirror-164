import os
import time
import json

from machine import Pin, SoftI2C

from modcore import modc, Module, LifeCycle, deprecated
from modcore.util import ensure_dirs, OS_SEP

from moddev.timeout import Timeout

from moddev.ntp import ntp_serv, NTP_EVENT

# from moddev.ntp_tz import ntp_tz_serv

from modlib.bosch.bmp280 import BMP280

SD_CARD = "/sd"
TEMPR = "tempr-"


class TempRec(Module):
    def watching_events(self):
        return [NTP_EVENT]

    def conf(self, config=None):
        super(Module, self).conf(config)

        self._timeout = config.get("tempr_timeout", 15)
        self._timebase = config.get("tempr_timeout:timebase", 60 * 1000)

        self.timeout = Timeout(self._timeout, timebase=self._timebase)

        self.i2c_addr = config.get("tempr:addr", 0x76)
        self.i2c_scl = config.get("tempr:scl", 15)
        self.i2c_sda = config.get("tempr:sda", 13)
        self.i2c_freq = config.get("tempr:freq", 400000)

        self.dest = config.get("tempr_dest", "/var/tempr")
        self.use_sd = config.get("tempr_sd_relative", True)
        self.max_keep = config.get("tempr_max_keep", 24 * 4 * 2)
        # time stamp generation utc, or localtime (False)
        self.tempr_utc = config.get("tempr_utc", True)

        self.i2c_dev = None
        self.ntp = None
        self.bmp = None

        self._err = False

    def start(self):

        if self.use_sd:
            if not self.check_sd_path():
                self._err = "no sd card found"
                self.use_sd = False
                self.warn(self._err)

        self.init_sensor()

    def init_sensor(self):
        try:
            self.i2c_dev = SoftI2C(
                freq=self.i2c_freq, scl=Pin(self.i2c_scl), sda=Pin(self.i2c_sda)
            )
            self.bmp = BMP280(self.i2c_dev, addr=self.i2c_addr)
        except Exception as ex:
            self.i2c_dev = None
            self.bmp = None
            self._err = str(ex)
            self.warn(self._err)

    def loop(self, config=None, event=None):

        if self.current_level() != LifeCycle.RUNNING:
            return

        if self.ntp is None and event:
            if self.is_event(event, NTP_EVENT):
                val = self.event_value(event)
                if val:
                    self.ntp = True

        if self.ntp is None:
            # never received NTP event
            return

        if self.timeout.elapsed():
            self.measure_save()
            self.timeout.restart()

    def stop(self):
        self.i2c_dev = None
        self.bmp = None

    def measure_save(self):
        try:
            now, tempr, press = self.measure()
            self.info("tempr,press: ", tempr, press)
            self.write_stat(now, tempr, press)
            return now, tempr, press
        except Exception as ex:
            self._err = str(ex)
            self.warn(self._err)

    def measure(self):
        if self.bmp is None:
            self.init_sensor()
        if self.bmp is None:
            raise Exception("no sensor found")

        now = ntp_serv.utctime() if self.tempr_utc else ntp_serv.localtime()
        tempr = self.bmp.temperature
        press = self.bmp.pressure / 100.0
        return now, tempr, press

    def write_stat(self, now, tempr, press):
        fnam = self.build_fnam(now)
        fnam = self.build_path(fnam)
        o = self.pack(now, tempr, press)
        try:
            ensure_dirs(fnam)
            with open(fnam, "w") as f:
                ostr = json.dumps(o)
                f.write(ostr)
            self.clean_tempr()
        except Exception as ex:
            self.warn("discard", o)
            self._err = str(ex)
            self.warn(self._err)

    def pack(self, now, tempr, press):
        return {
            "time": now[0:6],
            "temperature": tempr,
            "pressure": press,
            "utc": self.tempr_utc,
        }

    def check_sd_path(self):
        try:
            st = os.stat(SD_CARD)
            if st[0] == 16384:
                return True
        except:
            pass
        return False

    def build_fnam(self, now):
        fnam = "{tempr}{Y:04}{M:02}{D:02}-{h:02}{m:02}{s:02}.json".format(
            tempr=TEMPR, Y=now[0], M=now[1], D=now[2], h=now[3], m=now[4], s=now[5]
        )
        return fnam

    def build_path(self, fnam):
        fp = SD_CARD if self.use_sd else ""
        fp = fp + self.dest + OS_SEP + fnam
        return fp

    def iter_rec(self):
        fnam = self.build_path("")
        try:
            le = os.listdir(fnam)
            for e in le:
                if e.startswith(TEMPR):
                    yield fnam + e
        except Exception as ex:
            self._err = str(ex)
            self.warn(self._err)

    def pop_rec(self):
        try:
            fnam = next(self.iter_rec())
            with open(fnam) as f:
                data = f.read()
                data = json.loads(data)
        except Exception as ex:
            data = {"err": str(ex)}
        try:
            self.info("remove data", fnam, data)
            os.remove(fnam)
        except Exception as ex:
            self.warn("remove data", ex)
        return data

    def print_all_rec(self):
        for e in self.iter_rec():
            print(e)

    def clean_tempr(self):
        le = list(self.iter_rec())
        le = sorted(le)
        while len(le) > self.max_keep:
            e = le.pop(0)
            os.remove(e)
            self.info("removed old data", e)


temp_rec = TempRec("temprec")
modc.add(temp_rec)
