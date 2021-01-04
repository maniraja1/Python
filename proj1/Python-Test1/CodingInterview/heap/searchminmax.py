'''
Given an array find the min and max in the array

Below algorithm is called as the tournament method. You compare successive elements
and then compare the smallest with the global.small and largest with global.large.
If you follow a traditional alogorthm you need 2(n-2) comparisons. However with
tournament method you need 3 comparisons for every 2 elements.

Time Complexity: O(n)
'''

import collections
minmax = collections.namedtuple('minmax', ['smallest', 'largest'])

def findminmax(array: list):

    if array[0]<array[1]:
        global_minmax=minmax(array[0], array[1])
    else:
        global_minmax = minmax(array[1], array[0])

    for i in range(2, len(array)-1,2):
        #print(i, array[i], array[i+1])
        if array[i] < array[i+1]:
            local_minmax = minmax(array[i], array[i+1])
        else:
            local_minmax = minmax(array[i+1], array[i])
        #print(local_minmax)
        if global_minmax.smallest > local_minmax.smallest:
            global_minmax= minmax(local_minmax.smallest, global_minmax.largest)
        if global_minmax.largest < local_minmax.largest:
            global_minmax = minmax(global_minmax.smallest, local_minmax.largest)

    if len(array)%2 != 0:
        if global_minmax.smallest > array[-1]:
            global_minmax= minmax(array[-1], global_minmax.largest)
        if global_minmax.largest < array[-1]:
            global_minmax = minmax(global_minmax.smallest, array[-1])
    print(global_minmax)

x=[1,2,-3,8,5,6,7,-10]
findminmax(x)