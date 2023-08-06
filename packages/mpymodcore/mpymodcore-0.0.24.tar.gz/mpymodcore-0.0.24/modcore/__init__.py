"""
    (c)2020-2022 K. Goger - https://github.com/kr-g

https://github.com/kr-g/mpymodcore

License under:
https://github.com/kr-g/mpymodcore/blob/master/LICENSE

"""

from .cntrl import modc
from .mod import Module
from .lifecycle import LifeCycle
from .log import DEBUG, INFO, NOTSET, WARNING, ERROR, CRITICAL, logger

import time

VERSION = "v0.0.24"

_this_year = 2022  # time.localtime(time.time())[0]

print("-" * 41)
print("mpy modcore")
print("(c) 2020-" + str(_this_year) + " K. Goger")
print("version  ", VERSION)
print("homepage ", "https://github.com/kr-g/mpymodcore")
print("legal    ", "https://github.com/kr-g/mpymodcore/blob/master/LICENSE")
from .lic import *

print("-" * 41)


def deprecated(f):
    # @functools.wraps(f)
    def inner(*argv, **kwargs):
        import sys

        print(
            "warning: deprecated. call to ",
            f.__class__,
            f.__name__,
            " : ",
            f,
            file=sys.stdout,
        )
        return f(*argv, **kwargs)

    return inner


def untested(f):
    # @functools.wraps(f)
    def inner(*argv, **kwargs):
        print(
            "error: untested call to ",
            f.__class__,
            f.__name__,
            " : ",
            f,
            file=sys.stderr,
        )
        return f(*argv, **kwargs)

    return inner
