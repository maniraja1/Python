'''
Immutable class can be created in one of 2 ways
1. overwrite __setattr__
2. define a frozen data class
'''
from dataclasses import dataclass
class vector:

    def __init__(self, x , y):
        object.__setattr__(self, 'x', x)
        object.__setattr__(self, 'y', y)

    def __setattr__(self, key, value):
        raise NotImplementedError

    def __str__(self):
        return f"vector(x={self.x},y={self.y})"

@dataclass(frozen=True)
class vector2:
    x: int
    y: int


v1 = vector(7,8)
print(v1)
#v1.x = 100
print(v1)
v2 = vector2(8,9)
print(v2)
#v2.x = 100
print(v2)