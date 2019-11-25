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
        return self.function(*args, **kwargs)
        # We can also add some code
        # after function call.


# adding decorator to the class
@MyDecorator
def function(name, message='Hello'):
    print("{}, {}".format(message, name))


function("geeks_for_geeks", "hello")


# CLASS BASED DECORATOR using __get__
# Example 3.0
print('EXAMPLE 3.0')

class class_property:

    def __init__(self, getter):
        self._getter = getter

    def __get__(self, obj, cls):
        print(obj)
        print(cls)
        return self._getter(cls)

class BankAccount:
    accounts = []

    def __init__(self, balance=0):
        self.balance = balance
        self.accounts.append(self)
    @class_property
    def balance(cls):
        return sum(a.balance for a in cls.accounts)

account1 = BankAccount(balance=95)
account2 = BankAccount(balance=53)

print(BankAccount.balance)
print(account1.balance)
print(account1.balance)

# CLASS BASED DECORATOR using __call__
# Example 4.0
print('EXAMPLE 4.0')
class class_property3:

    def __init__(self, getter):
        self._getter = getter

    def __call__(self, obj, cls):
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
print(BankAccount3.total_balance)