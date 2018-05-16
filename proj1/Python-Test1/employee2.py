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

#### Example of class that does not have encapsulation for class attributes
#### Also you are able to set the properties outside of the class
q1 = Q(2000)
q1.y

### Example of how to fix data encapsulation
### However any code that was using p1.x=1 is now broken. Interfaces of setting the properties on a class are now broken
p1=P(1000)
print(p1.get_x())
## p1.x


### Example of how to fix data encapsulation
### Also now the interfaces are fixed r1.z is now available
### After adding the decorators now the functions getter and setter are not available outside
### However now the properties can be set in multiple ways
r1=R(10001)
print(r1.z)
r1.z=200
print(r1.z)

#### This has the same effect as the previous example
#### This is the same code as class P but now we can access X outside the class
#### The other advantage is we can now access getter and setter outside the class unlike in class R
s1=S(10001)
print(s1.x)
s1.x=300
print(s1.get_x())
s1.set_x(600)
print(s1.get_x())

#### Previous example however has a problem where a class properties can be set using r1.z and r1.set_z
t1=T(500)
print(t1.x)
t1.x=700
print(t1.x)

#### The right way to defie class and attributes is however in the example followed in Class R


