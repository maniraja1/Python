from functools import wraps, update_wrapper
class count_calls:
    def __init__(self,function):
        self.calls = 0
        self.function = function
        update_wrapper(self, function)

    def __call__(self,*args, **kwargs):
        self.calls += 1
        return self.function(*args, **kwargs)

def func_count_calls(func):
    """Record calls to the given function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

''' Main Problem
counter = count_calls()
print(counter.calls)
counter()
counter()
print(counter.calls)

counter = func_count_calls()
print(counter.calls)
counter()
counter()
print(counter.calls)
'''
''' BONUS 1
import random
rand = count_calls(random.random)
print(rand())
print(rand.calls)
print(rand())
print(rand.calls)

rand = func_count_calls(random.random)
print(rand())
print(rand.calls)
print(rand())
print(rand.calls)
'''
''' BONUS 2'''
@count_calls
def greet():
    print("Hello world")

greet()
print(greet.calls)
greet()
greet()
print(greet.calls)




