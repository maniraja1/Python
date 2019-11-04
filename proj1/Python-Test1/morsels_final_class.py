
'''
Using meta class to prevent subclassing.
This will fail when defining the class
'''
class UnsubclassableType(type):
    def __new__(cls, name, bases, classdict):
        for b in bases:
            if isinstance(b, UnsubclassableType):
                raise TypeError("type '{0}' is not an acceptable base type".format(b.__name__))
        return type.__new__(cls, name, bases, dict(classdict))


class Base(metaclass=UnsubclassableType):
    pass

'''
class MyClass(Base):
    pass
'''


'''
    Python morsels solution
'''

import time

#   Prevent Subclassing but do not generate an error when the child class is defined.
#   Instead only raise an error when the child class is instantiated

class Unsubclassable:
    def __new__(cls, *args, **kwargs):
        cls.printclass()
        cls.printsub()
        if cls is not Unsubclassable:
            raise TypeError(
                "type 'Unsubclassable' is not an acceptable base type"
            )
        return super().__new__(cls, *args, **kwargs)

    @classmethod
    def printclass(cls):
        print(f"ClassName:{cls.__name__}")

    @classmethod
    def printsub(subclass):
        print(f"Subclass Name: {subclass.__name__}")

class test(Unsubclassable):
    pass


Unsubclassable()
# test()


#   Create a base class which when subclassed raises an error as soon as the child class is defined
#   Notice the use of __init_subclass__

class Unsubclassable2:
    def __init_subclass__(cls, **kwargs):
        raise TypeError(
                "type 'Unsubclassable' is not an acceptable base type"
            )

# class MyClass(Unsubclassable2):
#     pass

time.sleep(1)
#   Create a decorator that prevents subclassing
def final_class(cls):
    print("Inside decorator")
    @classmethod
    def no_subclass(subclass2):
        class_name = cls.__name__
        subclass_name = subclass2.__name__
        raise TypeError(f"Class {subclass_name} cannot subclass {class_name}")
    cls.__init_subclass__ = no_subclass
    return cls


class test:
    pass


@final_class
class Unsubclassable3:
    print("Unsubclassable3")



Unsubclassable3()
print(Unsubclassable3.__dict__)
print(test.__dict__)

time.sleep(1)

class Myclass3(Unsubclassable3):
    pass
