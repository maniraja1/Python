'''
if you want to create a class that behaves like a set  you can inherit from Mutableset. In the below example we
create a class that behaves like a set and a sequence at the same time
Sets are not a sequence because sets do not guarantee ordering
Sequence are datastructures where ordering is guaranteed, whereas collections don't have order

List, typle are examples of sequence
sets, dicts are examples of collections

MutableSet Abstract methods are __Contains__, __iter__, __len__, add, discard

'''





from collections.abc import MutableSet

class KeyValueError(KeyError, ValueError):
    """Both a KeyError and a ValueError."""

class Orderedset2(MutableSet):

    def __init__(self, iterable=()):
        self.items = set()
        self.order = list()
        for item in iterable:
            self.add(item)

    def add(self, item):
        if item not in self.items:
            self.order.append(item)
            self.items.add(item)

    def discard(self, item):
        if item in self.items:
            self.order.remove(item)
            self.items.remove(item)

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.order)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (
                    len(self) == len(other) and
                    all(x == y for x, y in zip(self, other))
            )
        return super().__eq__(other)

    def __getitem__(self, index):
        return self.order[index]

    def __repr__(self):
        return f"{type(self).__name__}({self.order})"

    def __and__(self, other):
        return super(Orderedset2, other).__and__(self)

    def count(self, item):
        return int(item in self)

    def append(self, item):
        if item in self.items:
            raise ValueError(f"{item!r} already in OrderedSet")
        self.add(item)

    def remove(self, item):
        try:
            super().remove(item)
        except KeyError as e:
            raise KeyValueError(str(e)) from e


s1 = Orderedset2([1, 2, 3, 3, 3, 100, 99])
print(s1)
s2 = Orderedset2([1, 10,20,30,1000,990])
print(s2)
print(s1 & s2)
print(s1.count(3))
s1.append(500)
print(s1)
s1.remove(500)
print(s1)
'''
x={1,2,3,3,3,100,99}
print(type(x))
print(x)
y = (1,2,3,100,99)
print(type(y))
print(y)
'''