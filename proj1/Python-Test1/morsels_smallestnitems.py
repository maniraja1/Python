from collections.abc import Iterable
from heapq import nsmallest,heapify,heappop,heappush
import heapq
def min_n(x,y,key=None):
    if not isinstance(x,Iterable):
        raise Exception("first argument must be a collection")
    z = []
    while (len(z) < y and len(x)>0):
        val = [x[0], 0]
        for i,l in enumerate(x):
            if key is None :
                if l < val[0]:
                    val=[l,i]
            else:
                if key(l)<key(val[0]):
                    val=[l,i]
        z.append(val[0])
        del x[val[1]]
    return z

'''
Use the utilities from heapq to get the n smallest elements
'''
def min_n2(x,y,*,key=None):
    return nsmallest(y,x,key)



class Miniheap:

    def __init__(self,iterable):
        self.heap=iterable
        heapify(self.heap)
    def push(self,item):
        heappush(self.heap,item)

    def pop(self):
        return heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def popn(self,n):
        x = []
        for i in range(n):
            x.append(self.pop())
        return x

class Maxheap:

    def __init__(self,iterable):
        self.heap = iterable
        heapq._heapify_max(self.heap)

    def pop(self):
        return heapq._heappop_max(self.heap)

    def push(self,item):
        heapq.heappush(self.heap,item)
        heapq._heapify_max(self.heap)

    def popn(self,n):
        x = []
        for i in range(n):
            x.append(self.pop())
        return x

print(min_n([11, 2, 5, 1, 3, 8, 1], 3))
print(min_n([11, 2, 5, 1, 3, 8, 1], 10))

fruits = ['Watermelon', 'blueberry', 'lime', 'Lemon', 'jujube']
print(min_n(fruits, 3))
fruits = ['Watermelon', 'blueberry', 'lime', 'Lemon', 'jujube']
print(min_n(fruits, 3,key=str.lower))
fruits = ['Watermelon', 'blueberry', 'lime', 'Lemon', 'jujube']
print(min_n2(fruits, 3,key=str.lower))
numbers=[11, 2, 5, 1, 3, 8, 6]
heap1=Miniheap(numbers)
print(heap1.pop())
heap1.push(1)
print(heap1.pop())
print(heap1.peek())
print(heap1.pop())
print(heap1.pop())
numbers=[11, 2, 5, 1, 3, 8, 1]
heap2=Miniheap(numbers)
print(heap2.popn(3))
numbers=[11, 2, 5, 1, 3, 8, 1]
heap3=Maxheap(numbers)
print(heap3.pop())
heap3.push(100)
print(heap3.pop())


'''
https://en.wikipedia.org/wiki/Heap_(data_structure)
https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/articles/data_structures.html#article-data-structures
https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/Queue/index.html#queue-priorityqueue
'''

