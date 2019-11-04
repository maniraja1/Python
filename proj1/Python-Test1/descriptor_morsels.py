''' Solution 1'''
class PositiveNumber:

    def __init__(self,initial_value=None):
        self.value=initial_value
        self.c = 1


    def __get__(self, obj, obj_type):
        print(self.c)
        if(self.value != None):
            return self.value
        else:
            raise AttributeError(f"'{obj_type.__name__}' Object has no attribute '{self.name}'")

    def __set__(self, instance, value):
        print(f"setting value {value}")
        if(value > 0):
            self.value=value
        else:
            raise ValueError("Positive integer required")

    def __set_name__(self, obj_type, name):
        self.name = name

class Point:
    x=PositiveNumber(2)
    y=PositiveNumber()

''' solution 2'''
from abc import abstractmethod,ABC
class Validator(ABC):

    """Base class for descriptors that validate data assigned to them."""

    def __init__(self, initial=None):
        self.value = initial

    def __get__(self, obj, obj_type):
        if self.value is None:
            raise AttributeError(f"'{obj_type.__name__}' object has no attribute '{self.name}'")
        return self.value

    def __set__(self, obj, value):
        self.validate(value)
        self.value = value

    def __set_name__(self, obj_type, name):
        self.name = name

    @abstractmethod
    def validate(self,value):
        pass

class PositiveNumber2(Validator):

    """Descriptor which can only be assigned to positive numbers."""

    def validate(self, value):
        if value <= 0:
            raise ValueError("Positive integer required.")

class PositiveNumber3(Validator):
     def validate(self,value):
         pass

class point2:
    x = PositiveNumber2(2)
    y = PositiveNumber2()

class point3:
    x = PositiveNumber3(2)
    y = PositiveNumber3()

p=Point()
print(p.x)
p.x=4
print(p.x)
#print(p.y)

p=point2()
p.x=4
print(p.x)
#print(p.y)

p=point3()
p.x=4
print(p.x)
#print(p.y)
