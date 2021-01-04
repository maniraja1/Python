
def reloopable(fileobj:str):
    return list(fileobj)

class reloopable2:
    """Iterable which resets a file each time it's looped over."""
    def __init__(self, file_obj):
        self.lines = file_obj

    def __iter__(self):
        self.lines.seek(0)
        for line in self.lines:
            yield line


class reloopable3:

    """Iterable which resets a file each time it's looped over."""

    def __init__(self, file_obj):
        self.file = file_obj
        self._iterator = None

    def reset(self):
        self.file.seek(0)
        for line in self.file:
            yield line

    def __iter__(self):
        if self._iterator:
            self._iterator.close()  # This will only close the generator and not the file
        self._iterator = self.reset()
        return self._iterator

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.file.close()


from collections.abc import Iterable, Iterator
from contextlib import AbstractContextManager
import time


class ClosableIterator(Iterator):

    """Iterator which can be ended by calling the `close` method."""
    """Iterator class you do not have to implement __iter__"""

    def __init__(self, iterator, strict=False):
        self._iterator = iterator
        self._closed = False
        self.strict = strict

    def __next__(self):
        if self._closed:
            exc_type = RuntimeError if self.strict else StopIteration
            raise exc_type("Iterator stale")
        return next(self._iterator)

    def close(self):
        self._closed = True


class reloopable4(Iterable, AbstractContextManager):

    """Iterable which resets a file each time it's looped over."""
    """AbstractContextManger does not require __enter__ """
    def __init__(self, file_obj, strict=False):
        self.file = file_obj
        self._iterator = None
        self.strict = strict

    def __iter__(self):
        if self._iterator:
            self._iterator.close()
        self.file.seek(0)
        self._iterator = ClosableIterator(self.file, strict=self.strict)
        return self._iterator

    def __exit__(self, *args):
        self.file.close()

file = open('data/file.txt')
x=reloopable(file)
print(" ".join(x).replace("\n", ""))
print(" ".join(x).replace("\n", ""))
file.close()
print('#'*50)

file = open('data/file.txt')
x=reloopable2(file)
print(" ".join(x).replace("\n", ""))
print(" ".join(x).replace("\n", ""))
file.close()
print('#'*50)

file = open('data/file.txt')
x=reloopable2(file)
print(" ".join(x).replace("\n", ""))
print(" ".join(x).replace("\n", ""))
file.close()
print('#'*50)

with reloopable3(open('data/file.txt')) as x:
    print(" ".join(x).replace("\n", ""))
    print(" ".join(x).replace("\n", ""))
#print(" ".join(x).replace("\n", ""))
print('#'*50)

with reloopable4(open('data/file.txt')) as x:
    print(" ".join(x).replace("\n", ""))
    print(" ".join(x).replace("\n", ""))
print('#'*50)

with reloopable4(open('data/file.txt'), strict=True) as x:
    print(" ".join(x).replace("\n", ""))
    print(" ".join(x).replace("\n", ""))