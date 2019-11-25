import time
'''
Introduction
    Descriptor are object attribute with binding behavior. @property is a descriptor

Modules

Methods
    __get__, __set__, __delete__

Notes
    The most obvious use case is to build logic on how class properties should behave.
    One example is to raise error when negative values are set on  attributes

    Example 1.0
    non data descriptor on methods to control what is returned
    For more examples follow exercise Morsels_propertydecorator

    Example 2.0
    data descriptor to build property like class


'''
# Example 1.0
# Non data descriptor
class DoubleEverything:

    def __init__(self,getter,fset=None,fdel=None):
        self._getter = getter

    def __get__(self, instance, cls):
        val = self._getter(instance)*2
        return val


class account:
    def __init__(self,accountid,value):
        self.accountid=accountid
        self.accountvalue=value

    @DoubleEverything
    def doubleaccountvalue(self):
        return self.accountvalue


account1=account(1, 30)
print(f"AccountValue:{account1.doubleaccountvalue}")
print('##########################################################')
time.sleep(2)
# Example 2.0
# Data descriptor

class spl_property2(object):
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc


    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        print("inside __set__")
        if self.fset is None:
            raise AttributeError("can't set attribute")
        if value < 0:
            raise AttributeError("Value can't be negative")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        print(fget)
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)

class bankaccount:
    def __init__(self,accid,accbal):
        self.accid = accid
        self._balance = accbal

    @spl_property2
    def accid(self):
        return self._accid

    @accid.setter
    def accid(self,value):
        self._accid = value


b1=bankaccount(11, 100)
print("retrieving property accid")
print(b1.accid)
print(b1._balance)
time.sleep(2)
b1.accid=-11