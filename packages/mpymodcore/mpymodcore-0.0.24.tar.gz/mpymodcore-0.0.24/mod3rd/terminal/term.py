import uasyncio as asyncio
import gc
import time

from modcore.log import logger

try:
    from iolang import interprets
except:
    from modext.iotk.iolang import interprets

_stop_all = None

# using telnet port
# todo change port no
PORT = 23

port = PORT


def read_passwd():
    try:
        with open("terminal.cfg") as f:
            cont = f.read()
            lines = map(lambda x: x.strip(), cont.split("\n"))
            lines = filter(lambda x: len(x) > 0, lines)
            credits = list(lines)
            return credits[0]
    except:
        pass
    try:
        from term_cfg import PASS

        return PASS
    except:
        pass


async def auth(reader, writer):
    global passwd
    if passwd is None:
        return True
    logger.info("password", passwd)

    no_try = 3

    while True:
        try:
            await writer.awrite("password:\n")
            line = await reader.readline()
            line = line.decode()
            pw = line.strip()
            logger.info("got", pw)
            if pw == passwd:
                logger.info("authenticated")
                await writer.awrite("OK\n")
                break
            no_try = no_try - 1
            if no_try <= 0:
                await writer.awrite("too much atemps. bye.\n")
                return False
            await writer.awrite("try again\n")
        except Exception as ex:
            logger.excep(ex)
            return False
    return True


async def serv_func(reader, writer):
    logger.info("start terminal serv_func")

    if await auth(reader, writer):
        await writer.awrite("hola!\n")
        while True:
            try:
                line = await reader.readline()

                if len(line) == 0:
                    break

                line = line.decode().upper()
                cmd = line.strip()

                if cmd == "STOP":
                    break

                if len(cmd) == 0 or cmd == "EOT":
                    break

                try:
                    logger.info("execute", cmd)
                    rc = await interprets(cmd)
                except Exception as ex:
                    rc = "ERR:" + str(ex)

                logger.info("result", rc)

                # await writer.awrite(line)
                await writer.awrite(str(rc) + "\n")

            except Exception as ex:
                logger.info(ex)
                break

    await writer.wait_closed()
    logger.info("stop serv_func")


async def term_task(self):

    self.info("terminal task started")

    global passwd
    passwd = read_passwd()

    try:
        global port
        self.serv = asyncio.start_server(serv_func, "0.0.0.0", port)
        self.serv_t = asyncio.create_task(self.serv)
        self.info("started terminal async server", port)
        while True:
            if self.stop_sig.is_set():
                break
            await asyncio.sleep(1)
        self.info("terminal async routine cancel")
        self.serv_t.cancel()
        self.serv.cancel()

    except Exception as ex:
        self.excep(ex, "terminal async routine")
    self.info("terminal async routine stopping")
