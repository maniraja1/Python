from timeit import Timer


def test1():
    l=[]
    for i in range(1000):
        l=l+[i*2]
    print(l)
def test2():
    l=[]
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("concat ",t2.timeit(number=1), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("concat ",t3.timeit(number=1), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("concat ",t4.timeit(number=1), "milliseconds")



t5=Timer("l.pop()","l = list(range(10000))")
print("pop ",t5.timeit(number=1), "milliseconds")

t6=Timer("l.pop(1)","l = list(range(10000))")
print("pop(1) ",t6.timeit(number=1), "milliseconds")

