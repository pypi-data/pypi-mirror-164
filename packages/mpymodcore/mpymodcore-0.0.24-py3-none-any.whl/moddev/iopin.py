from machine import Pin

_hw_pins = {}


def _get_hw_pin(pin_no):
    return "Pin(" + str(pin_no) + ")"


def reset_cached(pin_no):

    pin_id = _get_hw_pin(pin_no)

    global _hw_pins
    if pin_id in _hw_pins:
        pin = _hw_pins.pop(pin_id)
        pin._init()


class IOPin(object):
    def __init__(self, pin_no, in_out_mode=-1, pull_mode=-1):
        self.pin_no = pin_no
        self.in_out_mode = in_out_mode
        self.pull_mode = pull_mode

        self.handler = None

        self.set_neglogic(False)

        self._open()

        global _hw_pins
        _hw_pins[str(self.pin)] = self

    def __repr__(self):
        return (
            self.__class__.__name__
            + "("
            + str(self.pin_no)
            + ", "
            + self.mode_str()
            + ("" if self.handler is None else ", IRQ")
            + ")"
        )

    def mode_str(self):
        return "OUT" if self.in_out_mode == Pin.OUT else "IN"

    def set_neglogic(self, neglogic=True):
        # defines the signaled state to negative logic
        self.neglogic = neglogic
        return self

    def _init(self):
        self.pin.irq(None)
        if self.in_out_mode == Pin.OUT:
            self.pin(0)
        self.pin.init()

    def _open(self):
        self._close()
        self.pin = Pin(self.pin_no, mode=self.in_out_mode, pull=self.pull_mode)

    def _close(self):
        reset_cached(self.pin_no)
        self.pin = None

    def value(self, val=None):
        if val is not None:
            return self.pin.value(val)
        return self.pin.value()

    def signaled(self, state=None):
        if state is not None:
            return self.value(bool(state) ^ bool(self.neglogic))
        return bool(self.value()) ^ bool(self.neglogic)

    def __call__(self, val=None):
        return self.signaled(val)

    def irq(self, handler=None, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING):
        self.pin.irq(handler=None, trigger=trigger)
        self.handler = handler
        if handler:
            self.pin.irq(handler=_hw_handler, trigger=trigger)
        return self


def _hw_handler(hw_pin):

    pin_id = str(hw_pin)

    global _hw_pins
    if pin_id in _hw_pins:
        pin = _hw_pins[pin_id]
        handler = pin.handler
        if handler:
            handler(pin)


def reset_cached_all():
    global _hw_pins
    for pin in _hw_pins.values():
        reset_cached(pin.pin_no)


def get_all():
    return _hw_pins.values()


def get_all_in():
    return list(filter(lambda x: x.in_out_mode == Pin.IN, get_all()))


def get_all_out():
    return list(filter(lambda x: x.in_out_mode == Pin.OUT, get_all()))


def get_pin(pin_no, in_out_mode=-1, pull_mode=-1):

    pin_id = _get_hw_pin(pin_no)

    global _hw_pins
    if pin_id in _hw_pins:
        pin = _hw_pins[pin_id]
        if pin.in_out_mode == in_out_mode:
            return pin
    pin = IOPin(pin_no, in_out_mode=in_out_mode, pull_mode=pull_mode)
    return pin


def get_pin_out(pin_no, pull_mode=-1, neglogic=False):
    pin = get_pin(pin_no, in_out_mode=Pin.OUT, pull_mode=pull_mode)
    return pin


def get_pin_in(pin_no, pull_mode=-1, neglogic=False):
    pin = get_pin(pin_no, in_out_mode=Pin.IN, pull_mode=pull_mode)
    return pin
