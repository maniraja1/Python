from dataclasses import dataclass, astuple
import copy
import pickle
'''
class Vector:
    __slots__ = ['x','y','z']


    def __init__(self, x, y, z):
        object.__setattr__(self, 'x', x)
        object.__setattr__(self, 'y', y)
        object.__setattr__(self, 'z', z)

    def __iter__(self):
        yield astuple(self)

    def __eq__(self, other):
        if isinstance(other, Vector):
            if list(self) == list(other):
                return True
            else:
                return False
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __add__(self, other):
        z = list()
        for i,_ in enumerate(self):
            z.append(list(self)[i]+list(other)[i])
        return Vector(*z)

    def __sub__(self, other):
        z = list()
        for i, _ in enumerate(self):
            z.append(list(self)[i] - list(other)[i])
        return Vector(*z)

    def __mul__(self, val):
        z = list()
        for i, _ in enumerate(self):
            z.append(list(self)[i] * val)
        return Vector(*z)

    def __rmul__(self, val):
        return self.__mul__(val)

    def __truediv__(self, val):
        z = list()
        for i, _ in enumerate(self):
            z.append(list(self)[i] / val)
        return Vector(*z)

    def __rtruediv__(self, val):
        return self.__truediv__(val)

    def __str__(self):
        return f" Vector ("+" ".join(str(list(self)))+")"

    def __setattr__(self, *args):
        raise NotImplementedError
'''


@dataclass(frozen=True)
class Vector2:

    x: float
    y: float
    z: float
    __slots__ = 'x', 'y', 'z'

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __eq__(self, other):
        if isinstance(other, Vector2):
            if list(self) == list(other):
                return True
            else:
                print(list(self))
                print(list(other))
                return False
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __add__(self, other):
        z = list()
        if isinstance(other, Vector2):
            for i, _ in enumerate(self):
                z.append(list(self)[i] + list(other)[i])
            return Vector2(*z)
        else:
            raise TypeError

    def __sub__(self, other):
        z = list()
        for i, _ in enumerate(self):
            z.append(list(self)[i] - list(other)[i])
        return Vector2(*z)

    def __mul__(self, val):
        z = list()
        for i, _ in enumerate(self):
            z.append(list(self)[i] * val)
        return Vector2(*z)

    def __rmul__(self, val):
        return self.__mul__(val)

    def __truediv__(self, val):
        z = list()
        for i, _ in enumerate(self):
            z.append(list(self)[i] / val)
        return Vector2(*z)

    def __rtruediv__(self, val):
        return self.__truediv__(val)

    def __copy__(self):
        return self

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





v = Vector2(1, 2, 3)
x, y, z = v
print(list(v))
print(x, y, z)
print(v == Vector2(1, 2, 4)) #False
print(v == Vector2(1, 2, 3))
print(v != Vector2(1, 2, 3)) # False
print(Vector2(1, 2, 3) + Vector2(4, 5, 6) == Vector2(5, 7, 9))
print(Vector2(5, 7, 9) - Vector2(3, 1, 2) == Vector2(2, 6, 7))
print(3 * Vector2(1, 2, 3) == Vector2(3, 6, 9))
print(Vector2(1, 2, 3) * 2 == Vector2(2, 4, 6))
print(Vector2(1, 2, 3) / 2 == Vector2(0.5, 1, 1.5))
print(2/Vector2(1, 2, 3) == Vector2(0.5, 1, 1.5))
print(v)
object.__setattr__(v, 'x', 3)
object.__setattr__(v, 'y', 4)
object.__setattr__(v, 'z', 5)
print(v)
v = Vector2(1, 2, 3)
v2 = Vector2(3, 4, 5)
vector_set = {v, v2}
print(Vector2(1, 2, 3) in vector_set)
v3 = copy.copy(v2)
v4 = copy.deepcopy(v2)
print('#'*50)
print(f"Original {v2}")
print(f"Copy: {v3}")
print(f"Deepcopy: {v4}")
object.__setattr__(v2, 'x', 6)
object.__setattr__(v2, 'y', 7)
object.__setattr__(v2, 'z', 8)
print('#'*50)
print(f"Original {v2}")
print(f"Copy: {v3}")
print(f"Deepcopy: {v4}")
print('#'*50)
data = pickle.dumps(v)
w = pickle.loads(data)
print(w)
print(w==v)
print(w is v)