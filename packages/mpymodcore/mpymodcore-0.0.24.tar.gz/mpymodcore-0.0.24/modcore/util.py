import os

OS_SEP = "/"


def get_stat(fnam):
    try:
        return os.stat(fnam)
    except:
        return None


def is_file(fnam, st=None):
    if st is None:
        st = os.stat(fnam)
    return st[0] == 32768


def is_dir(fnam, st=None):
    if st is None:
        st = os.stat(fnam)
    return st[0] == 16384


def ensure_dirs(fnam):
    el = fnam.split(OS_SEP)[0:-1]
    fn = ""
    for e in el:
        if e == "":
            continue
        fn = fn + OS_SEP + e
        st = get_stat(fn)
        if st:
            if is_dir(fn, st):
                continue
            raise Exception("not a folder", fn)
        os.mkdir(fn)
