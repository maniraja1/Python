import heapq
def sortincreasingdecreasing(array: list)->list:
    sorted_subarray=[]
    innerarray=[]
    type=None
    prev = None
    for x in array:
        print(type, x, prev)

        if prev is None:
            prev = x
            innerarray.append(x)
            continue

        if type is None:
            if x>prev:
                type='increasing'
            else:
                type='decreasing'


        if x>prev and type=='increasing':
            innerarray.append(x)
            prev=x
        elif x>prev and type=='decreasing':
            sorted_subarray.append(innerarray[::-1])
            innerarray = []
            innerarray.append(x)
            prev=x
            type='increasing'

        elif x<prev and type=='decreasing':
            innerarray.append(x)
            prev=x
        elif x<prev and type=='increasing':
            sorted_subarray.append(innerarray)
            innerarray=[]
            innerarray.append(x)
            prev = x
            type = 'decreasing'
    if x>prev and type=='decreasing':
        sorted_subarray.append(innerarray)
    else:
        sorted_subarray.append(innerarray[::-1])
    print(ksortedarray(sorted_subarray))

def ksortedarray(arrays:list)->list:
    min=[]
    result = []
    heapq.heapify(min)
    sorted_array = [iter(x) for x in arrays]

    for i,x in enumerate(sorted_array):
        heapq.heappush(min, (next(x),i))

    print(min)

    while len(min)>0:
        val,i = heapq.heappop(min)
        result.append(val)
        try:
            nextelement=next(sorted_array[i])
            heapq.heappush(min, (nextelement, i))
        except StopIteration:
            continue
    return result






x=[57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
sortincreasingdecreasing(x)