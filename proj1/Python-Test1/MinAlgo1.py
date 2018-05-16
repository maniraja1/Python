import time
def findmin2():
    start=time.time()
    list=[10,11,20,4,5,1,1,1,1,1]
    iter=0
    min = 0

    for i in range(len(list)):

        for j in range (len(list)):
            iter=iter+1
            if list[j]<list[i]:
                min=list[j]
    print("Min value is : {0}".format(min))
    print(iter)
    end=time.time()

    print(end-start)

findmin2()

def findmin1():
    start = time.time()
    list = [10,11,20,4,5,1,1,1,1,1]
    iter = 0
    min=list[0]
    for i in range(len(list)):
        iter=iter+1
        if list[i] < min:
            min = list[i]

    print("Min value is : {0}".format(min))
    print(iter)
    end=time.time()

    print(end-start)

findmin1()


