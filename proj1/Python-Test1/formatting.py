list=[1,3,2,4,1,2]
tuple=(1,3,2,4,1,2)
set={1,3,2,4,1,2}
dict={'name':'mani','age':35}
print(list)
print(tuple)
print(set)
print(dict['name'])



dict={'name':'mani','age':35}
s= "Name is {0}, Age is {1}".format(dict['name'],dict['age'])
print(s)

dict={'name':'mani','age':35}
s= "Name is {0[name]}, Age is {0[age]}".format(dict)
print(s)

l= ['mani',35]
s= "Name is {0[0]}, Age is {0[1]}".format(l)
print(s)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1 = person('mani',36)

s= "Name is {0.name}, Age is {0.age}".format(p1)
print(s)


s= "Name is {name}, Age is {age}".format(name='mani',age=38)
print(s)


dict={'name':'mani','age':35}
s= "Name is {name}, Age is {age}".format(**dict)
print(s)


for i in range(20):
    print("The number is {:03}".format(i))

pi=3.144484495959550505
print("pi={:0.3f}".format(pi))

print("Bank balance is {:,.3f}".format(1000000*10))

import datetime
my_date=datetime.datetime(2018,5,22,10,00,00)
print(my_date)

s="The date is {}".format(my_date)
print(s)

s="The date is {:%B %d %Y}".format(my_date)
print(s)