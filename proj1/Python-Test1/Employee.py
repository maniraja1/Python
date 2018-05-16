class employee:
    companyname1 = "test"
    raiseamount = 1.04

    def __init__(self , name):
        self.employeename=name

    @classmethod
    def setcompanyname (cls,compname):
        cls.companyname=compname
    @classmethod
    def setraiseamount (cls,amt):
        cls.raiseamount = amt
    def printcompanyname(self):
        print(self.companyname)

class developer(employee):
    pass


emp1 = employee('test20')
emp2 = employee('test200')

emp3 = developer('dev20')
emp4 = developer('dev200')

print(help(developer))

'''
print((dir(emp1)))
print(emp1.employeename)
print(getattr(emp1,'employeename'))
setattr(emp1,'employeeage',40)
print(getattr(emp1,'employeename'))
setattr(emp1,'employeename','test2')
print(getattr(emp1,'employeename'))
print(getattr(emp1,'employeeage'))

print(emp1.raiseamount)

print(emp1.companyname1)
print(getattr(employee,'companyname1'))
print(employee.companyname1)

print(emp2.raiseamount)

print(emp2.companyname1)

emp1.setcompanyname('salesforce')
emp1.setraiseamount(1.05)
emp1.address='Test address'
print(emp1.raiseamount)
print(emp1.companyname)
print(emp1.address)
print(emp2.raiseamount)
print(emp2.companyname)
##print(emp2.address)
'''