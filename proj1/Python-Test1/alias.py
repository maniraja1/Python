
from operator import attrgetter

def alias1(attr):
    def geter(self):
        return eval(f'self.{attr}')
    return property(geter)

def alias2(attr):
    return property(lambda self: getattr(self, attr))

def alias3(self, attr):
    return getattr(self,attr)

def alias4(attr):
    return  getattr(self, attr)

def alias5(attr):
    return property(attrgetter(attr))

def attrsetter(attr):
    def setter(obj, value):
        setattr(obj, attr, value)
    return setter


def alias7(attr, *, write=False):
    if write:
        return property(attrgetter(attr), attrsetter(attr))
    else:
        return property(attrgetter(attr))

'''class to handle descriptors instance variable only. '''
class alias:

    def __init__(self,attr):
        self.attr=attr

    def __get__(self, instance, owner):
        return getattr(self,self.attr)

    def __set__(self,obj,value):
        raise AttributeError("Cannot set alias")

'''Class to handle descriptors instance variable only with truthy writes'''
class aliascls2:
    def __init__(self,attr,*,write=False):
        self.attr=attr
        self.write=write
    def __get__(self,obj,obj_type):
        return getattr(obj,self.attr)
    def __set__(self,obj,value):
        if not self.write:
            raise AttributeError("Cannot set alias")
        setattr(obj,self.attr,value)

'''Class to handle descriptors both instance and class variables with truthy writes'''
class aliascls3:
    def __init__(self, attr, write=False):
        self.attr = attr
        self.write = write

    def __get__(self, obj, obj_type):
        if obj is not None:
            return getattr(obj, self.attr)
        else:
            return getattr(obj_type, self.attr)

    def __set__(self, obj, value):
        if not self.write:
            raise AttributeError("Cannot set alias")
        setattr(obj, self.attr, value)

class emp:

    title = alias1( 'serial')
    title2=alias2('serial')
    #title3=alias3(self,  'serial')
    #title4 = alias4( 'serial')
    title5 = alias5('serial')
    title6=alias('serial')
    title7=alias7('serial',write=True); '''Truthy write implementation function'''
    title8=aliascls2('serial',write=True); '''Truthy write implementation class'''
    def __init__(self, serial):
        self.serial = serial





x=emp('abc')
print(x.title)
print(x.title5)
print(x.title7)
print(x.title8)
print(x.serial)
x.serial='xyz'
print(x.title)
print(x.title5)
print(x.title7)
print(x.title8)
print(x.serial)
'''In the following example when you change the value for the alias it autoatically changes the variable value as well'''
x.title7='v'
print(f"Title7:{x.title7}")
print(f"Title8:{x.title8}")
print(f"serial:{x.serial}")
x.title8='w'
print(f"Title7:{x.title7}")
print(f"Title8:{x.title8}")
print(f"serial:{x.serial}")
print(f"title:{x.title}")

