import time
class class_property:

    def __init__(self, getter):
        self._getter = getter

    def __get__(self, obj, cls):
        print(obj)
        print(cls)
        return self._getter(cls)


class class_property2(class_property):

    def __get__(self, obj, cls):
        print(obj)
        print(cls)
        # This is to make the property a class only property
        if obj is not None:
            raise AttributeError('This is a "class only" property')
        return self._getter(cls)

class class_property3:

    def __init__(self, getter):
        self._getter = getter

    def __call__(self, *args, **kwargs):
        return self._getter(*args, **kwargs)

class BankAccount:
    accounts = []

    def __init__(self, balance=0):
        self.balance = balance
        self.accounts.append(self)
    @class_property
    def balance(cls):
        return sum(a.balance for a in cls.accounts)

class BankAccount2:
    accounts = []

    def __init__(self, balance=0):
        self.balance = balance
        self.accounts.append(self)
    @class_property2
    def total_balance(cls):
        return sum(a.balance for a in cls.accounts)

class BankAccount3:
    accounts = []

    def __init__(self, balance=0):
        self.balance = balance
        self.accounts.append(self)

    @class_property3
    def total_balance(cls):
        return sum(a.balance for a in cls.accounts)

@class_property3
def xtest(i):
    return  i*i

account1 = BankAccount(balance=95)
account2 = BankAccount(balance=53)

print(BankAccount.balance)
print(account1.balance)
print(account1.balance)
print(account1.__dict__)
print(account2.__dict__)
print(BankAccount.__dict__)

print('##############################################')
time.sleep(2)

account3 = BankAccount2(balance=95)
account4 = BankAccount2(balance=53)

print(BankAccount2.total_balance)
#print(account3.balance)
#print(account4.total_balance)

print('##############################################')
time.sleep(2)

account5 = BankAccount3(balance=95)
print(BankAccount3.total_balance)

print('##############################################')
time.sleep(2)
print(xtest(5))
