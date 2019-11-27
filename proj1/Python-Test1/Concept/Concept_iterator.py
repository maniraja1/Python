'''
Concept
    An iterable is anything you’re able to loop over.
    An iterator is the object that does the actual iterating.
    You can get an iterator from any iterable by calling the built-in iter function on the iterable.
    To make an iterator you could create an iterator class, a generator function, or a generator expression.


module

methods
    iter, next, yield
    __next__, __iter__

Notes
    There are several ways of
        iter, generator function, generator expression and iterator class
        Iter
            use iter to turn any iterable to an iterator.
            You can use next to get the next value.
            You can
            see Example 1.0
        generator expression
            you can create an expression that returns an iterator. This is very similar to list expression
            see example 2.0
        Generator function
            You can create a function that will return a generator object by using the yield keyword.
            You can convert any function to generator by using yield
            see Example 3.0
        Iterator class
            You can create a custom class that can behave like an iterator by implementing __iter__ and __next__
            See Example 4.0

    You can create a custom class that can behave as a generator or as an iterator
        Generator
            See example 5.0

        Iterator
            See Example 4.0

Additional reference
https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/


'''

# Example 1.0
print('###############################################')
print('Example 1.0')
i = [1,2,3,4]
print(f"This is a list {i}")
j = iter(i)
print(f"This is an iterator: {j}")
print(next(j))
print(next(j))
for x in j:
    print(x)

# Example 2.0
print('###############################################')
print('Example 2.0')
i=(n**2 for n in range(1, 10))
print(i)
print(next(i))
print(next(i))
for x in i:
    print(x)

# Example 3.0
print('###############################################')
print('Example 3.0')
def squares():
    for n in range(1000000):
        yield n**2

x=squares()
print(x)
print(next(x))
print(next(x))
print(next(x))

# Example 4.0
print('###############################################')
print('Example 4.0')
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


squares = Peekable(n**2 for n in [1, 2, 3, 4])
print(next(squares))
print(next(squares))
print(squares)
print(list(squares))


# Example 5.0
print('###############################################')
print('Example 5.0')
class Peekable2:

    def __init__(self, items):
        print(type(items))
        if isinstance(items, types.GeneratorType) or isinstance(items, Iterator):
            self.items=list(items)
        else:
            self.items=items
        self._ctr = 0

    def __iter__(self):
        while self._ctr < len(self.items):
            val= self.items[self._ctr]
            self._ctr += 1
            yield val

squares2 = Peekable2(n**2 for n in [1, 2, 3, 4])
print(list(squares2))
squares2 = Peekable2(n**2 for n in [1, 2, 3, 4])
for n in squares2:
    print(n)

