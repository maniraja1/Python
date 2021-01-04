'''
python has 3 ways how a class can be serialized/desrialized
1. Marshall (old do not use)
2. json(new, human readable,  limited support for data types)
3. pickle (preferred way, binary format not human readable)

pickle module has 4 methods
dump -> return file
pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
dumps -> returns string
pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None)
load -> load from file
pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)
loads -> loads from string
pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)

In case of a database connection or a file handle these objects cannot be pickled
You can use __getstate__() to define what should be included in the pickling process. This method allows you to
specify what you want to pickle.
If you don’t override __getstate__(), then the default instance’s __dict__will be used.

If you want to add some additional initializations while unpickling You can accomplish this with __setstate__()
'''
from pickle import dumps, loads
class Vector:

    def __init__(self):
        self.x = 100
        self.y = 200

    def __str__(self):
        return f"Vector(x={self.x},y={self.y})"
'''
v1 = Vector()
Pickledobject = dumps(v1)
v1.x = 300
print(v1)
v2 = loads(Pickledobject)
print(v2)
'''

# pickling with immutable class
class Vector2:

    def __init__(self, x, y):
        object.__setattr__(self, 'x', x)
        object.__setattr__(self, 'y', y)

    def __str__(self):
        return f"Vector(x={self.x},y={self.y})"

    def __setattr__(self, key, value):
        raise NotImplementedError

'''
v1 = Vector2(100,200)
Pickledobject = dumps(v1)
print(v1)
v2 = loads(Pickledobject)
print(v2)
'''

# with slots
class Vector3:
    __slots__ = 'x', 'y'

    def __init__(self):
        self.x = 100
        self.y = 200

    def __str__(self):
        return f"Vector(x={self.x},y={self.y})"

'''
v1 = Vector3()
#print(v1.__dict__)
Pickledobject = dumps(v1)
print(v1)
v2 = loads(Pickledobject)
print(v2)
'''

# with slots and immutable
class Vector4:
    __slots__ = 'x', 'y'

    def __init__(self):
        object.__setattr__(self, 'x', 100)
        object.__setattr__(self, 'y', 200)

    def __str__(self):
        return f"Vector(x={self.x},y={self.y})"

    def __setattr__(self, key, value):
        raise NotImplementedError

    def __getstate__(self):
        x = dict(
            (slot, getattr(self, slot))
            for slot in self.__slots__
            if hasattr(self, slot)
        )
        return x

    def __setstate__(self, state):
        for slot, value in state.items():
            object.__setattr__(self, slot, value)


v1 = Vector4()
#print(v1.__dict__)
Pickledobject = dumps(v1)
print(v1)
v2 = loads(Pickledobject)
print(v2)


