from collections.abc import Iterable
from functools import partial
import re

__all__ = [f'sm{"o" * i}sh' for i in range(2, 11)]

def __dir__():
    return __all__

def _flatten(input):
    out = list()
    for x in input:
        if isinstance(x, Iterable) and not (isinstance(x, str)):
            for y in x:
                out.append(y)
        else:
            out.append(x)
    return out

def _smoosher(input,counter):
    i = 1
    while i <= counter-1:
        out = _flatten(input)
        input = out
        i += 1
    else:
        out=input
    return out

def smoosh(input):
    i=1
    while i<=1:
        out = _flatten(input)
        input=out
        i += 1
    return out


def __getattr__(name):
    if re.search(r'^smoo+sh$', name):
        return partial(_smoosher, counter=name.count('o'))
    raise AttributeError(f"module {__name__} has no attribute {name}")


