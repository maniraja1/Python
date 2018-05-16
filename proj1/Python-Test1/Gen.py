import datetime
def timer(func):
    def wrapper(*args,**kwargs):
        t1=datetime.datetime.now()
        func(*args,**kwargs)
        t2=datetime.datetime.now()
        print("Start Time:{0}".format(t1))
        print("End Time:{0}".format(t2))
        print("Time taken in MicroSeconds:{0}".format(t2-t1))
    return wrapper

@timer
def square(x):
    result=[]
    for i in x:
        result.append(i*i)
    print(result)
    return result

@timer
def square_gen(x):
    for i in x:
        val = i*i
        yield()



square([i for i in range(10000)])

print(square_gen([1]))

for s in square_gen([1,2,3]):
    print (s)



