from math import pi,pow
from time import sleep
class circle:

    def __init__(self, radius=1):
        self.radius=radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        try:
            if radius <0:
                raise ValueError
            self.__radius=radius
            self.__diameter=radius*2
        except ValueError:
            raise ValueError ("Radius cannot be negative")


    @property
    def diameter(self):
        return self.__radius*2

    @diameter.setter
    def diameter(self,d):
        self.radius=d/2

    @property
    def area(self):
        return pi*pow(self.__radius, 2)









c1=circle(5)
print(c1.radius)
print(c1.diameter)
print(c1.area)

c1.radius=10
print(c1.radius)
print(c1.diameter)
print(c1.area)

c2=circle()
print(c2.radius)
print(c2.diameter)
print(c2.area)

print("Set diameter to 4 on C2")
c2.diameter=4
print(c2.radius)
print(c2.diameter)
print(c2.area)
'''
sleep(1)
c2.diameter=-1
print("Setting diameter to -1 on c2")
print(c2.radius)
print(c2.diameter)
print(c2.area)

sleep(1)
c3=circle(-1)
'''
