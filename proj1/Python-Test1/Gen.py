import datetime
def timer(func):
    def wrapper(*args,**kwargs):
        t1=datetime.datetime.now()
        out=func(*args,**kwargs)
        t2=datetime.datetime.now()
        print("Start Time:{0}".format(t1))
        print("End Time:{0}".format(t2))
        print("Time taken in MicroSeconds:{0}".format(t2-t1))
        return out
    return wrapper

@timer
def square(x):
    result=[]
    for i in x:
        result.append(i*i)
    ##print(result)
    return result

@timer
def square_gen(x):
    for i in x:
        yield (i*i)



'''X=square([i for i in range(10000)])
print(X)'''

## This is one way of calling generator
out=square_gen([1,2,3])
print(next(out))
print(next(out))
print(next(out))


### This is anoother way of calling a generator
out=square_gen([1,2,3])
for i in out:
    print(i)

## This returns the values
for s in square_gen([1,2,3]):
    print (s)

## This returns a generator object
print(s for s in square_gen([1,2,3]))

### This retruns a list
print("Return a list")
list1=[x*x for x in [1,2,3,4]]
print(list1)


### This returns a generator,
print("return a generator")
gen1=(x*x for x in [1,2,3,4]) ##notice "[]" has been replaced with "()"
print(gen1)
for i in gen1:
    print(i)





