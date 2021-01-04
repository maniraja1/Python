from functools import wraps
class positional_only:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        return self.func(*args)

def positional_only2(func):
    @wraps(func)
    def wrapper(*args):
        return func(*args)
    return wrapper

@positional_only
def add(x,y):
    return x+y

@positional_only2
def add2(x,y):
    return x+y


print(add(2, 3))
print(add2(2, 3))