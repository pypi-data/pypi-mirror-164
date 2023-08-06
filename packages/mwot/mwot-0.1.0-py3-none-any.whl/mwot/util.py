"""General functions, etc."""

import itertools
import warnings

from . import stypes


def chunks(it, size):
    """Chop an iterable into chunks of length `size`.

    Also yields the remainder chunk.
    """
    it = iter(it)
    while chunk := tuple(itertools.islice(it, size)):
        yield chunk


def chunk_bits(bits, chunk_size):
    """Break bits into chunks for encoding."""
    for chunk in chunks(bits, chunk_size):
        if len(chunk) < chunk_size:
            chunk += (0,) * (chunk_size - len(chunk))
            message = (f'word count not divisible by {chunk_size}; trailing '
                       f'zero(s) added')
            warnings.warn(message, RuntimeWarning)
        yield chunk


def deshebang(s, stype=None):
    """Remove a leading shebang line."""
    if stype is None:
        stype, s = stypes.probe(s)
    else:
        s = iter(s)
    shebang = stype.convert('#!')
    newline = stype.ord('\n')
    leading = stype.join(itertools.islice(s, len(shebang)))
    if leading == shebang:
        # Drop the rest of the line.
        for char in s:
            if char == newline:
                break
    else:
        yield from leading
    yield from s


def split(s):
    """Split a text string-like on whitespace."""
    s = iter(s)

    def nextword():
        for char in s:
            if not char.isspace():
                yield char
                break
        for char in s:
            if char.isspace():
                break
            yield char

    while word := ''.join(nextword()):
        yield word
