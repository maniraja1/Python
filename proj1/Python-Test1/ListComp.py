import datetime
def timer(func):
    def wrapper(*args,**kwargs):
        t1=datetime.datetime.now()
        func(*args,**kwargs)
        t2=datetime.datetime.now()
        print("Executing function {0}".format(func.__name__))
        print("Start Time:{0}".format(t1))
        print("End Time:{0}".format(t2))
        print("Time taken in MicroSeconds:{0}".format(t2-t1))
        print("-------------------------------------------------")
    return wrapper

@timer
def list1(x):
    result=[]
    for i in x:
        result.append(i*i)
    print(result)

list1([i for i in range(100)])

@timer
def list2(x):
    result=[i*i for i in x]
    print(result)

list2([i for i in range(100)])

@timer
def list3(x):
    result=[i for i in map(lambda i: i*i,x)]
    print (result)

list3([i for i in range(100)])


@timer
def list4(x):
    result=[i*i for i in x if i%2==0]
    print (result)

list4([i for i in range(100)])

@timer
def list5(x):
    result=[i*i for i in filter(lambda i:i%2==0,x)]
    print(result)

list5([i for i in range(100)])

@timer
def list6(x,y):
    result=[(i,j) for i in x for j in y]
    print(result)

list6([1,2,3,4],['a','b','c','d'])

@timer
def list7():
    name=['a','b','c','d']
    value=[10,20,30,40]
    print(zip(name,value)) ### Zip object
    print (list(zip(name,value))) ### Converting zip object to a list

    dict={}
    for name,value in list(zip(name,value)):
        dict[name]=value
    print(dict)

list7()

@timer
def list8():
    name = ['a', 'b', 'c', 'd']
    value = [10, 20, 30, 40]
    dict={name:value for name,value in list(zip(name,value))}
    print(dict)
list8()


@timer
def list9():
    myset = {i for i in range(10) if i%2==0}
    myset.add(11)
    myset.add(22)
    print(myset)

list9()

'''
@timer
def gen1(x):
    for i in range(x):
        print(i)
        yield i

mygen=gen1(10)
print(mygen)
for i in mygen:
    print(i)

def simple_generator_function():
    yield 1
    yield 2
    yield 3

for value in simple_generator_function():
    print(value)

our_generator = simple_generator_function()
next(our_generator)

@timer
def gen2():
    my_gen=(n*n for n in range(10))

for i in gen2():
    print (i)
'''