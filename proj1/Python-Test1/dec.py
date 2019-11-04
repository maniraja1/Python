##### Decorator
from functools import  wraps
def outer_func(func):
    @wraps(func)
    def inner_func(*args,**kwargs):
        print('Function {0} was executed inside of inner_func'.format(func.__name__))
        return func(*args,**kwargs)
    return inner_func

''''
@outer_func
def test_func(msg):
    print ("This is a test function. write something here")
    print(msg)

### Use this code if you dont use decortors
test=outer_func(test_func)
test("execute this code here")

### With Decorators
test_func("execute second code here")
'''
import functools
class decorator_class:

    def __init__(self,func):
        self.func=func
        ##functools.update_wrapper(self,func)

    def __call__(self, *args, **kwargs):
        print("Executed Function: {0}".format(self.func.__name__))
        return self.func(*args,**kwargs)
    def __name__(self):
        return(self.__name__())

class decorator2_class:
    def __init__(self,func):
        self.func=func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        print("Executed Function2: {0}".format(self.func.__name__))
        return self.func(*args,**kwargs)
    def __name__(self):
        return(self.__name__())

@decorator_class
@decorator2_class
def display_property(name,age):
    print("The Name is:{0}".format(name))
    print("The Age is:{0}".format(age))

display_property('mani',35)






