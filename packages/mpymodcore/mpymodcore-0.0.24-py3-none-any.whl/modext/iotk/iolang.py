import time
import machine
import uasyncio as asyncio

from moddev.iopin import get_pin_in, get_pin_out
from moddev.iopin import get_all_in, get_all_out
from moddev.iopin import reset_cached, reset_cached_all, get_all


class CommandNotFoundException(Exception):
    pass


class CommandAlreadyDefinedException(Exception):
    pass


_cmds = {}


def add_command(mnemonic, func, overwrite=False):
    if type(mnemonic) != list:
        mnemonic = [mnemonic]
    for mne in mnemonic:
        mne = mne.upper()
        if mne in _cmds and not overwrite:
            raise CommandAlreadyDefinedException("already declared", mne)
        _cmds[mne] = func


async def interpreta(args, _async=False):
    cmd = args.pop(0).upper()
    if cmd in _cmds:
        return await _cmds[cmd](args)
    raise CommandNotFoundException("Command not found", cmd)


async def interprets(inp):
    args = inp.split()
    return await interpreta(args)


async def interpret(inp):
    res = []
    for cmd in inp.split(";"):
        cmd = cmd.strip()
        if len(cmd) == 0:
            continue
        rc = await interprets(cmd)
        res.append(rc)
    return res


# helper and commands


def get_port(pnam):
    neglogic = pnam.startswith("!")
    if neglogic:
        pnam = pnam[1:]
    port = int(pnam)
    return neglogic, port


async def show(args):
    res = list(map(lambda x: (x.pin_no, x.mode_str()), get_all()))
    return res


async def reset(args):
    if len(args) == 0:
        args.append("ALL")
    for arg in args:
        if arg.upper() == "ALL":
            reset_cached_all()
            break
        neg, port = get_port(arg)
        reset_cached(port)

    res = []
    for pin in get_all():
        res.append((pin.pin_no, str(pin)))
    return res


async def get_io(args):
    res = []
    for arg in args:
        neg, port = get_port(arg)
        pin = get_pin_in(port)
        pin.set_neglogic(neg)
        res.append(pin())
    return res


async def set_io(args):
    res = []
    while len(args) > 0:
        neg, port = get_port(args.pop(0))
        pin = get_pin_out(port)
        pin.set_neglogic(neg)
        if len(args) == 0:
            nums = 1
        else:
            nums = args.pop(0)
        try:
            sign = int(nums)
            pin(sign)
            res.append(pin())
        except:
            res.append("*" + str(pin()))

    return res


async def clr_io(args):
    res = []
    for arg in args:
        neg, port = get_port(arg)
        pin = get_pin_out(port)
        pin.set_neglogic(neg)
        pin(0)
        res.append(pin())
    return res


async def neg_io(args):
    res = []
    for arg in args:
        neg, port = get_port(arg)
        pin = get_pin_out(port)
        pin.set_neglogic(neg)
        pin(not pin())
        res.append(pin())
    return res


async def trigger_io(args):
    res = []

    pins = []
    durs = []

    while len(args) > 0:
        arg = args.pop(0)
        neg, port = get_port(arg)
        pin = get_pin_out(port)
        pin.set_neglogic(neg)
        pins.append(pin)
        arg = args.pop(0)
        dur = float(arg)
        durs.append(dur)

    print(list(zip(pins, durs)))

    await asyncio.sleep(0)

    startt = time.ticks_ms()

    while len(pins) > 0:

        [x(1) for x in pins]

        mdur = min(durs)

        endt = time.ticks_add(startt, int(mdur * 1000.0))
        waitt = time.ticks_diff(endt, startt)

        if waitt > 0:
            await asyncio.sleep_ms(waitt)

        while len(pins) > 0:
            try:
                pos = durs.index(mdur)
                if pos < 0:
                    break
                pins[pos](0)
                pins.pop(pos)
                durs.pop(pos)
            except Exception as ex:
                print(ex)
                res = pins
                break

    return res


async def wait_sec(args):
    dur = float(args.pop(0))
    return await asyncio.sleep(dur)


async def reboot_machine(args):
    machine.reset()


# add the commands

add_command(["GET", "I", "G", "R"], get_io)
add_command(["SET", "O", "S", "W"], set_io)
add_command(["CLR", "C"], clr_io)
add_command(["FLIP", "F", "NOT", "N"], neg_io)
add_command(["RESET", "RST"], reset)
add_command(["T"], trigger_io)
add_command(["SHOW", "L", "LS"], show)

add_command(["WAIT"], wait_sec)
add_command(["REBOOT", "RESTART"], reboot_machine)
