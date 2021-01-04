from collections.abc import MutableSet, MutableSequence

class KeyValueError(KeyError, ValueError):
    """Both a KeyError and a ValueError."""

class OrderedSet:

    def __init__(self, iterable=()):
        self.items = set()
        self.order = list()
        for item in iterable:
            self.add(item)

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return len(self) == len(other) and all(x in other for x in self)
        return NotImplemented

    def __getitem__(self, index):
        return self.order[index]

    def __repr__(self):
        return f"{type(self).__name__}({self.order})"

    def add(self, item):
        if item not in self.items:
            self.order.append(item)
            self.items.add(item)

    def discard(self, item):
        if item in self.items:
            self.order.remove(item)
            self.items.remove(item)

class Orderedset2(MutableSequence, MutableSet):

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

    #Bonus1
    def __and__(self, other):
        print(super(Orderedset2, other))
        return super(Orderedset2, other).__and__(self)

    #Bonus2
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

    #Bonus3
    def __setitem__(self, index, value):
        if self.order[index] == value:
            return
        if value in self.items:
            raise ValueError(f"{value!r} already in OrderedSet")
        self.items.remove(self.order[index])
        self.order[index] = value
        self.items.add(value)

    def insert(self, index, item):
        if item in self.items:
            raise ValueError(f"{item!r} already in OrderedSet")
        self.order.insert(index, item)
        self.items.add(item)

    def remove(self, item):
        if item not in self.items:
            raise ValueError
        else:
            self.order.remove(item)
            self.items.remove(item)

    def discard(self,item):
        self.remove(item)

    def __delitem__(self, key):
        try:
            self.items.remove(self.order.pop(key))
        except:
            raise KeyError




