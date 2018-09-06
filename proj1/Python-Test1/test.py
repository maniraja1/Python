class employee:

    def __init__(self,fname,lname):
        self.first=fname
        self.__last=lname
        self.__email1=('{}.{}@gmail.com').format(self.first,self.last)



    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self,fname):
        if(fname == 'mani'):
            self.__first='cooldude'
        else:
            self.__first=fname

    @property
    def last(self):
        return self.__last

    @property
    def email1(self):
        return self.__email1

    @property
    def email2(self):
        return ('{}.{}@gmail.com').format(self.first,self.last)






e1=employee('mani','shankar')
print(e1.first)
e1.first='raja'

print(e1.first)
print(e1.last)
print(e1.email1)
print(e1.email2)


'''
e1.first= 'mani'

print(e1.first)
print(e1.last)
print(e1.email1)
print(e1.email2)
'''


''' Once you define an attribute as a property you cannot then set the attribute without a setter you will get an error
AttributeError: can't set attribute
Follow the example above and then comment out the @last.setter. you should get an error'''

'''
when you set define an attribute as a property and then define setter for this attribute. Anytime you set the value
inside the __init__ method you will see that it calls the setter and follows whatever code you have in there.
This is a good way to perform data encapsulation
If you would still like for init to set the attriute without following rules in the setter initially then you can add "__" beofre your attribute
This will make sure init bypasses data encapsulation, however any future modifications to the attribute would call the setter method
'''

from itertools import islice,repeat,chain

l=[1,2,3,4,5,6,7,8,9,10,11,12]
print(l)
for i,x in enumerate(islice(l,3)):
    print(x)



x=(1,2,3)
y=(4,5,6)

z=x+y
print(z)


z=(x+(None,)*3)
print(z)

for i,x in enumerate(islice(chain(l,repeat(None)),15)):
    print (x)


for i,x in enumerate(islice(chain('abc',repeat(-1,12)),15)):
    print(x)