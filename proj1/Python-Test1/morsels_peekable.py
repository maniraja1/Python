
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
