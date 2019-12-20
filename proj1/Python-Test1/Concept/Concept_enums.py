'''
Quick Concept
    Enums are lookup values assigned to members inside code
    Monday=1, Tuesday=2 .....
Modules
    from enum import Enum,unique,auto
    from enum import IntEnum
Properties
    There are 2 properties that helps with getting value from Enum. "name" & "value"
Methods


Notes:
        When using Enum you cannot have 2 objects with the same name, however you can assign the same id to 2 different objects.
        see Example 1.0 for more details
        You can force uniqueness on Enum by using decorator @unique.
        See Example 1.1
        If values don't matter you can use auto() to automatically provide an auto increment value
        See Example 1.2
        Subclassing of a base class that is a child of enum class is allowed. However you cannot extend enum values in the chilld class
        Enums are callable
        See Example 1.3
        IntEnum is a subclass of Enum and Int. Memnbers of IntEnum can be compared to Integers
        See Example 1.4
        You can also use IntFlag & Flag which are basically used for bitwise operators
'''
from enum import Enum,unique,auto
from enum import IntEnum

# Enum class
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(f'{Color.RED}')
print(f'Name: {Color.RED.name}')
print(f'Value: {Color.RED.value}')

# Supports iteration
for colors in Color:
    print(f'Color {colors.name} has a value of {colors.value}')

# example 1.0
# This is not allowed
print('#'*50)
print('#'*20, 'Example 1.0', '#'*20)
'''
class Shape(Enum):
    SQUARE = 2
    SQUARE = 3
'''
# This is allowed
class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2

# If uniqueness is desired you can use decorator @unique
# Example 1.1
print('#'*50)
print('#'*20, 'Example 1.1', '#'*20)
'''
@unique
class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2
'''
# Use Auto() for auto increment values
# Example 1.2
print('#'*50)
print('#'*20, 'Example 1.2', '#'*20)
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


for colors2 in Color:
    print(f'Color {colors2.name} has a value of {colors2.value}')

# Enums are callable
# Example 1.3
print('#'*50)
print('#'*20, 'Example 1.3', '#'*20)
Animal = Enum('x', 'ANT BEE CAT DOG')
for colors2 in Animal:
    print(f'Color {colors2.name} has a value of {colors2.value}')

# IntEnums
# Example 1.4
print('#'*50)
print('#'*20, 'Example 1.4', '#'*20)
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(f'Member of ENum: {Color.RED == 1}')

class Color(IntEnum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(f'Member of IntEnum: {Color.RED == 1}')








