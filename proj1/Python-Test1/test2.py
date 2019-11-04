from functools import  wraps
def cachedproperty(func):
    @wraps(func)
    def inner_func(*args,**kwargs):
        print('Function {0} was executed inside of inner_func'.format(func.__name__))
        return func(*args,**kwargs)
    inner_func

class test:
    def __init__(self,radius):
        self.radius=radius
    @property
    def diameter(self):
        return self.radius*2

class test_dec:
    def __init__(self,radius):
        self.radius=radius

    @cachedproperty
    def diameter(self):
        return self.radius*2

test1=test(5)
print(test1.radius)
print(test1.diameter)
#test1.diameter=20
print(test1.radius)
print(test1.diameter)

test1=test_dec(5)
print(test1.radius)
print(test1.diameter)
#test1.diameter=20
print(test1.radius)
print(test1.diameter)





x=slice(1,5,2)
print(x.indices(4))
for i in range(*x.indices(4)):
    print(i)

