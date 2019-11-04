class Cached_Property:
    def __init__(self,func):
        print(func)
        self.func=func  ##''' Note when we use decorator the func is passed in'''
        self.value=self.sentinel=object() ##''' sentinel is just to store the initial value and compare self.value with sentinel to see if value needs to be calculated'''
        self._getter=func ##'''setting getter to the function that is passed'''
        self._setter=self._deleter=None

    def setter(self,setter):
        print("Inside Setter")
        print(setter)
        self._setter = setter
        return self

    def deleter(self,deleter):
        self._deleter = deleter
        return self

    def __get__(self, instance, value=None):
        if instance is None:
            ##''' Notice return self if the function is called from a class and not the instance it returns the address and not the value'''
            return self
        if self.value is self.sentinel:
            self.value = self._getter(instance)
        else:
            self.value = self.func(instance)
        return self.value

    def __set__(self, instance, value):
        print("Inside Set")
        if self._setter:
            print("Setter exists")
            print(self._setter)
            self._setter(instance,value)
            self.value=self.sentinel
        else:
            self.value=value

    def __delete__(self,instance):
        self.value = self.sentinel
        if self._deleter:
            self._deleter(instance)



class Circle:
    def __init__(self,radius):
        self.radius=radius

    @Cached_Property
    def diameter(self):
        print("Inside Circle diameter")
        return self.radius*2

    @diameter.setter
    def diameter(self,diameter):
        if diameter < 0:
            raise ValueError("Diameter cannot be negative")
        else:
            self._diameter=diameter



c1 = Circle(5)
print("##############")
print(c1.radius)
print(c1.diameter)
c1.radius=6
print(c1.radius)
print(c1.diameter)
c1.diameter=20
print(c1.radius)
print(c1.diameter)
del c1.diameter
print(c1.radius)
print(c1.diameter)
print(Circle.diameter)
print(Circle.diameter.__get__(c1))