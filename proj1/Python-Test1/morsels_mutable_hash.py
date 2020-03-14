from collections.abc import MutableMapping
from reprlib import recursive_repr

def mutable_hash(thing):
    #print(f"Thing: {thing}")
    if isinstance(thing, (list, tuple)):
        x=tuple(mutable_hash(v) for v in thing)
        y=hash(x)
        #print(f"tuple: {x}, hash: {y}")
        return y
    elif isinstance(thing, dict):
        return hash(frozenset(
            (k, mutable_hash(v))
            for k, v in thing.items()
        ))
    elif isinstance(thing, set):
        return hash(frozenset(thing))
    #print ('else')
    return hash(thing)

class HashWrapper:
    def __init__(self, obj):
        self.data = obj

    def __eq__(self, other):
        if isinstance(other, HashWrapper):
            return self.data.__eq__(other.data)
        return self.data.__eq__(other)

    def __hash__(self):
        return mutable_hash(self.data)

class UnsafeDict(MutableMapping):

    def __init__(self, data={}):
        self._data = data
        # self.update(data)

    def __getitem__(self, key):
        return self._data[HashWrapper(key)]

    def __setitem__(self, key, value):
        self._data[HashWrapper(key)] = value

    def __delitem__(self, key):
        del self._data[HashWrapper(key)]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for key in self._data:
            yield key.data

    @recursive_repr()
    def __repr__(self):
        items = ", ".join(
            f"{key!r}: {value!r}"
            for key, value in self.items()
        )
        return "{" + items + "}"


d = UnsafeDict()
d[[1,2]]='x'
d[[3,4]]='y'

print(d)

for x in d:
    print(x, d[x])

x= mutable_hash([1,2,[3,4,[5,6]], [5,6]])
print(x)


