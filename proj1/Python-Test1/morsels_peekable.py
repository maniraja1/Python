
import types
import time
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

    def peek(self):
        if len(self.items) > 0:
            return self.items[self._ctr]

    def __bool__(self):
        if self._ctr >= len(self.items):
            return False
        else:
            return True

    def prepend(self, val):
        self.items.insert(self._ctr, val)

    def __getitem__(self, item):
        if isinstance(item,slice):
            if item.start is None:
                start=self._ctr
                if item.stop is not None:
                    stop = item.stop+self._ctr
            else:
                raise ValueError ("Start index should always be None")
            if item.step is not None:
                raise ValueError ("Step should be None")

            return self.items[start: stop: item.step]
        else:
            if item >= 0:
                start=item+self._ctr
                return self.items[item]
            else:
                raise ValueError ("Cannot have negative index")



print('###############################################')
squares = Peekable(n**2 for n in [1, 2, 3, 4])
print(next(squares))
print(squares.peek())
print(squares.peek())
print(next(squares))
print(squares)
print(list(squares))
print('###############################################')
# Bonus1.0
squares = Peekable(n**2 for n in [1, 2, 3, 4])
for n in squares:
    print(n, end=" ")
    if squares:
        print("followed by", squares.peek())
    else:
        print("and we're done")
print('###############################################')
# Bonus2.0
words = Peekable(["3", "blue", "purple", "2", "green"])
for word in words:
    if word.isdigit() and words:
        for n in range(int(word)-1):
            words.prepend(words.peek())
    else:
        print(word)
print('###############################################')
# Bonus3.0
words = Peekable(["2", "blue", "blue", "3", "green", "pink", "red"])
print(words[0])
print(next(words))
print(words[:2])
print('###############################################')
time.sleep(2)
x=iter([1,2,3])
print(x)
print(list(x))
iterator = Peekable(iter([]))
print(iterator.peek())



'''
Morsels solution
Main difference in comparison to above solution is 
we use peek and store the next value in self.cache and __next__ would return the value from self.cache
we use dequeue 
we use islice
'''

from collections import deque
from itertools import islice


SENTINEL = object()


class peekable:

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.cache = deque()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.cache:
            self.peek()
        return self.cache.popleft()

    def __bool__(self):
        try:
            self.peek()
        except StopIteration:
            return False
        return True

    def __getitem__(self, index):
        if isinstance(index, slice):
            assert index.start in (None, 0) and index.step in (None, 1)
            stop = index.stop - len(self.cache)
        else:
            assert index >= 0
            stop = index+1 - len(self.cache)
        self.cache.extend(islice(self.iterator, max(stop, 0)))
        if isinstance(index, slice):
            return list(islice(self.cache, *index.indices(index.stop)))
        else:
            return self.cache[index]

    def peek(self, default=SENTINEL):
        if not self.cache:
            try:
                self.cache.append(next(self.iterator))
            except StopIteration:
                if default is not SENTINEL:
                    return default
                raise
        return self.cache[0]

    def prepend(self, value):
        self.cache.appendleft(value)