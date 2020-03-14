'''
Quick Concept
    Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function or class.

Modules

Methods
    __call__, __get__
Properties

Notes
    you can create decorators from function or from classes
    FUNCTION BASED DECORATOR
        See Example 1.0
        You trap func in the outer function and then call the function in the inner function
    CLASS BASED DECORATOR
        There are 2 ways to create class based decorators. One using __call__ and another using __get__
        __call__
            You use __call__ when the decor is used by a function. When you use this in a class decor returns an
            address instead of returning the value
            see Example 2.0
            you have a __call__ method that defines what you want to do before and after function call
            you trap the func name in __init__ and then call the function inside __call__
        __get__
            Use __get__ when you want to use the decor on class and instance of class.
            see Example 3.0
            This is used to create a property based decorator
            you trap the func name in __init__ and then call the function inside __get__

        See Example 4.0
        This is to show that using __call__ with a call does not return the value but just an address

    There are more examples that can be found here
    https://www.geeksforgeeks.org/class-as-decorator-in-python/

'''
# Function based decorator
# Example 1.0
print('EXAMPLE 1.0')
import inspect
def our_decorator(func):
    print(func.__name__)
    print([locals()[x] for x in inspect.getfullargspec(func).args])

    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        func(*args, **kwargs)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Hi")


# CLASS BASED DECORATOR using __call__
# Example 2.0
print('EXAMPLE 2.0')
class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # We can add some code
        # before function call
        print("Code  that runs before")
        return self.function(*args, **kwargs)
        print("Code that runs after")
        # We can also add some code
        # after function call.


# adding decorator to the class
@MyDecorator
def function(name, message='Hello'):
    print("{}, {}".format(message, name))


function("geeks_for_geeks", "hello")


# CLASS BASED DECORATOR using __get__
# This will not work if the class has parameters that are passed
# Example 3.0
print('EXAMPLE 3.0')

class class_property:

    def __init__(self, getter):
        self._getter = getter

    def __get__(self, obj, cls):
        return self._getter(cls)

class BankAccount:
    accounts = []

    def __init__(self, balance=0):
        self.balance = balance
        self.accounts.append(self)


    @class_property
    def Totalbalance(cls):
        return sum(a.balance for a in cls.accounts)

account1 = BankAccount(balance=95)
account2 = BankAccount(balance=53)
print("############")
print(BankAccount.Totalbalance)
print("############")
print(account1.balance)
print(account2.balance)

# CLASS BASED DECORATOR using __call__
# Note that in this case it returns address and not values
# Example 4.0
print('EXAMPLE 4.0')
class class_property3:

    def __init__(self, getter):
        self._getter = getter

    def __call__(self, cls):
        print("Inside call")
        #print(obj, cls)
        return self._getter(cls)

class BankAccount3:
    accounts = []

    def __init__(self, balance=0):
        self.balance = balance
        self.accounts.append(self)

    @class_property3
    def total_balance(cls):
        return sum(a.balance for a in cls.accounts)

account5 = BankAccount3(balance=95)
print(account5.balance)
print("############")
print(BankAccount3.total_balance)
print("############")

print("Example 5.0")
import time
class InstanceTracker:

    def __init__(self, getter):
        self._getter = getter

    def __call__(self,  x):
        print(self.__dict__)
        self._args = x
        print(self._getter)
        print(f"Args: {self._args}")
        return self._getter(self._args)

    def __get__(self, instance, owner):
        print(instance)
        print(owner)
        self._cls = owner
        print(self._getter)
        return self._getter(instance)



@InstanceTracker
def testfunc(x):
    return x

print(testfunc(5))



print("Example 6.0")

class BankAccount2:

    def __init__(self, bal):
        self.balance=bal

    @InstanceTracker
    def total(self):
        return self.balance
'''
    # This will throw error
    @InstanceTracker
    def total2(self,x):
        print(x)
        return self.balance
'''

print("This only works with instance methods does not work when parameters are passed other than self")
a1 = BankAccount2(10)
print(a1.total)

# Example where methods can pass parameters and decorator can process the parameter.
print("Example 7.0")

def our_decorator(func):
    instances = []
    print(func.__name__)
    #print([locals()[x] for x in inspect.getfullargspec(func).args])

    def function_wrapper(self, *args, **kwargs):
        print("Before calling " + func.__name__)
        instances.append(self)
        return func(self, *args, **kwargs)
    return function_wrapper


class BankAccount:
    @our_decorator
    def __init__(self, bal):
        self.balance=bal

    @our_decorator
    def getbalance(self, x):
        print(x)
        return self.balance

    @our_decorator
    def total(self):
        return self.balance

print("This  works with instance methods and methods with parameters.")
a = BankAccount(5)
time.sleep(1)
b = BankAccount(6)
time.sleep(1)
print(a.getbalance(1))
print(b.getbalance(2))
print(a.total())
print(b.total())


print("Example 8.0")
def track_instances(cls):
    original_init = cls.__init__
    cls.instances = []
    def __init__(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        cls.instances.append(self)
    cls.__init__ = __init__
    return cls

@track_instances
class bankaccount:
    def __init__(self, bal):
        self.bal=bal

a=bankaccount(10)
b=bankaccount(20)

print(bankaccount.instances)