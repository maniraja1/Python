from math import pi,pow

class Q:
    def __init__(self,y):
        self.y=y

class P:
    def __init__(self,x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
               self.__x = x

class R:

    def __init__(self,z):
        self.z = z

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z):
        if z < 0:
            self.__z = 0
        elif z > 1000:
            self.__z = 1000
        else:
            self.__z = z

class S:
    def __init__(self, x):
        self.set_x(x)
    def get_x(self):
        return self.__x
    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(get_x, set_x)

class T:
    def __init__(self, x):
        self.__set_x(x)
    def __get_x(self):
        return self.__x
    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(__get_x, __set_x)


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

#### Example of class that does not have encapsulation for class attributes
#### Also you are able to set the properties outside of the class
print('q1')
q1 = Q(2000)
print(q1.y)

### Example of how to fix data encapsulation
### However any code that was using p1.x=1 is now broken. Interfaces of setting the properties on a class are now broken
print('p1')
p1=P(1000)
print(p1.get_x())
## p1.x


### Example of how to fix data encapsulation
### Also now the interfaces are fixed r1.z is now available
### After adding the decorators now the functions getter and setter are not available outside
### However now the properties can be set in multiple ways
print('r1')
r1=R(10001)
print(r1.z)
r1.z=200
print(r1.z)

#### This has the same effect as the previous example
#### This is the same code as class P but now we can access X outside the class
#### The other advantage is we can now access getter and setter outside the class unlike in class R
print('s1')
s1=S(10001)
print(s1.x)
s1.x=300
print(s1.get_x())
s1.set_x(600)
print(s1.get_x())

#### Previous example however has a problem where a class properties can be set using r1.z and r1.set_z
print('t1')
t1=T(500)
print(t1.x)
t1.x=700
print(t1.x)

#### The right way to defie class and attributes is however in the example followed in Class R


### Dynamic parameters
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


