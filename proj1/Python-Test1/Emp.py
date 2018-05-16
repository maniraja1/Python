class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name (self,name):
        self.__name=name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age=age

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,salary):
        self.__salary=salary


    def __repr__(self):
        return ("employee ({}, {}, {})").format(self.name,self.age,self.salary)

    def __str__(self):
        return ("Name:{}, Age:{}, Salary:{}").format(self.name,self.age,self.salary)


class engineer(employee):

    def __init__(self,name,age,salary,language):
        super().__init__(name,age,salary)
        self.language=language

    @property
    def language(self):
        return self.__language
    @language.setter
    def language(self,language):
        self.__language=language

    def __repr__(self):
        return("engineer({},{},{},{})").format(self.name,self.age,self.salary,self.language)
    def __str__(self):
        return ("Name:{},Age:{},Salary:{},Language:{}").format(self.name,self.age,self.salary,self.language)

class manager(employee):
    def __init__(self,name,age,salary,employees=[]):
        super().__init__(name,age,salary)
        self.employees=employees
    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self,employees):
        if (employees is None):
            self.__employees=[]
        else:
            self.__employees=employees


eng1 = engineer('mani',35,160000,'python')
eng2 = engineer('suba',30,130000,'tableau')
eng3 = engineer('manager',45,200000,'java')

manager1=manager(eng3.name,eng3.age,eng3.salary,employees=[])

print(manager1.name)
print(manager1.employees)

print(eng1)
print(eng1.__repr__())
