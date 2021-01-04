from dataclasses import dataclass


class Vector:
    __slots__ = ['items']


    def __init__(self, x, y, z):
       object.__setattr__(self, 'items', [x,y,z])

    def __getitem__(self, item):
        return self.items[item]

    def __eq__(self, other):
        if isinstance(other, Vector):
            if self.items == other.items:
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
        for i,_ in enumerate(self.items):
            z.append(self.items[i]+other.items[i])
        return Vector(*z)

    def __sub__(self, other):
        z = list()
        for i, _ in enumerate(self.items):
            z.append(self.items[i] - other.items[i])
        return Vector(*z)

    def __mul__(self, val):
        z = list()
        for i, _ in enumerate(self.items):
            z.append(self.items[i] * val)
        return Vector(*z)

    def __rmul__(self, val):
        return self.__mul__(val)

    def __truediv__(self, val):
        z = list()
        for i, _ in enumerate(self.items):
            z.append(self.items[i] / val)
        return Vector(*z)

    def __rtruediv__(self, val):
        return self.__truediv__(val)

    def __str__(self):
        return f" Vector ("+" ".join(str(self.items))+")"

    def __setattr__(self, *args):
        raise NotImplementedError



v = Vector(1, 2, 3)
x, y, z = v
print(x, y, z)
print(v == Vector(1, 2, 4))
print(v == Vector(1, 2, 3))
print(v != Vector(1, 2, 3))
print(Vector(1, 2, 3) + Vector(4, 5, 6) == Vector(5, 7, 9))
print(Vector(5, 7, 9) - Vector(3, 1, 2) == Vector(2, 6, 7))
print(3 * Vector(1, 2, 3) == Vector(3, 6, 9))
print(Vector(1, 2, 3) * 2 == Vector(2, 4, 6))
print(Vector(1, 2, 3) / 2 == Vector(0.5, 1, 1.5))
print(2/Vector(1, 2, 3) == Vector(0.5, 1, 1.5))
print(v)
object.__setattr__(v, 'items', [3,4,5])
print(v)