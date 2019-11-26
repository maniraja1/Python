'''
Concept
    An iterable is anything you’re able to loop over.
    An iterator is the object that does the actual iterating.
    You can get an iterator from any iterable by calling the built-in iter function on the iterable.

module

methods
    iter, next
    __next__, __iter__

Notes
    use iter to turn any iterable to an iterator.
    You can use next to get the next value.
    You can
    see Example 1.0

    You can create a custom class that can behave like an iterator by implementing __iter__ and __next__
    See Example 2.0
'''

# Example 1.0
print('')
i = [1,2,3,4]
print(f"This is a list {i}")
j = iter(i)
print(f"This is an iterator: {j}")
print(next(j))
print(next(j))
for x in j:
    print(x)

# Example 2.0
import types
from collections.abc import Iterable, Iterator
class Peekable:

    def __init__(self, items):
        print(type(items))
        if isinstance(items, types.GeneratorType) or isinstance(items, Iterator):
            self.items=list(items)
        else:
            self.items=items
        self._ctr = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._ctr >= len(self.items):
            raise StopIteration
        val= self.items[self._ctr]
        self._ctr += 1
        return val

print('###############################################')
squares = Peekable(n**2 for n in [1, 2, 3, 4])
print(next(squares))
print(next(squares))
print(squares)
print(list(squares))
print('###############################################')
