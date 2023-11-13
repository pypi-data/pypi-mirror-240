#!/usr/bin/env python3

__all__ = [
    'bytes',
]

import io
import os
import pathlib
import builtins

def bytes(arg):
    if isinstance(arg, io.IOBase):
        arg = arg.read()
    if isinstance(arg, str):
        arg = arg.encode()
    if isinstance(arg, pathlib.Path):
        arg = arg.as_posix()
    if os.path.exists(arg):
        arg = open(arg, 'rb').read()
    if isinstance(arg, builtins.bytes):
        return arg
    cls = type(arg)
    raise FileNotFoundError(f"Could not cast to bytes: {cls.__name__!r}")
