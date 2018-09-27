import itertools
from collections import Iterable

def length(*args):
    print("Running Length with input:", args)
    totallength = 0
    for i in args:
        print("Value of i:", i)
        if isinstance(i, Iterable) and len(i) > 1:
            totallength += length(*i)
            print("TotalLengthinner:", totallength)
        else:
            totallength += 1
        print("TotalLength:", totallength)
    return totallength



print(length([4, 5],[8, 9],6,7,8,'helloworld'))

