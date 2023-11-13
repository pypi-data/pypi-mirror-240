import os
import sys
import assure

def make_stream(mode):
    return os.fdopen(os.popen("echo hello world").fileno(), mode)

def test_assure_stream():
    stream = make_stream('r')
    assert not stream.seekable()
    stream = make_stream('r')
    assert assure.seekable(stream).seekable()

    stream = make_stream('rb')
    assert not stream.seekable()
    stream = make_stream('rb')
    assert assure.seekable(stream).seekable()

    bytes = f"hello world"
    assert assure.seekable(bytes).seekable()
