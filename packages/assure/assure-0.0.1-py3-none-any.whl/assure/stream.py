__all__ = [
    'seekable',
    'mode',
]

import os
import io

def seekable(o):
    if hasattr(o, 'seekable'):
        if o.seekable():
            return o
        if o.mode == 'r':
            return io.StringIO(o.read())
        if o.mode == 'rb':
            return io.BytesIO(o.read())
        raise TypeError(f"cannot assure seekable: {o}")
    raise TypeError(f"input is not a stream: {o}")

def mode(o, mode):
    if not hasattr(o, 'mode'):
        raise TypeError(f"input has no mode attribute: {o}")
    if o.mode == mode:
        return o
    return os.fdopen(o.fileno(), mode)

