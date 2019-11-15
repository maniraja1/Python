import time
class decorator_class:
    def __init__(self,func):
        self.func=func

    def __call__(self, *args, **kwargs):
        print("Executed Function: {0}".format(self.func.__name__))
        print(f"{args}")
        return self.func(*args, **kwargs)

    def __name__(self):
        return(self.__name__())

class test:

    def __init__(self, account):
        self.account=account

    @decorator_class
    def Totalaccount(self):
        print('returning account')
        return self.account

@decorator_class
def display_property(name,age):
    print("The Name is:{0}".format(name))
    print("The Age is:{0}".format(age))

display_property('mani', 36)
time.sleep(1)
'''
account1=test(100)
print(account1.account)
print(account1.Totalaccount())
'''
class decorator2:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print
        'instance %s of class %s this is now decorated whee!' % (
            self.obj, self.cls
        )
        return self.func.__call__(*args, **kwargs)

    def __get__(self, instance, owner):
        self.cls = owner
        self.obj = instance

        return self.__call__

class test2:

    def __init__(self, account):
        self.account=account

    @decorator2
    def Totalaccount(self):
        print('returning account')
        return self.account

account2=test2(200)
print(account2.Totalaccount())



