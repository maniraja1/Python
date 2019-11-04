import heapq
import random

def klargestitem(array,k):
    heap =[]
    for i in array:
        if len(heap)>0:
            x=heap[0]
        else:
            x=-1
        if i > x:
            if len(heap)>= k:
                heapq.heappop(heap)
            heapq.heappush(heap,i)
    return heap

array2=range(100*100)
random.shuffle(list(array2))

print(klargestitem(array2,3))