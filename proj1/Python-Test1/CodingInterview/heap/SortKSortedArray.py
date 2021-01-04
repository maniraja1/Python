import heapq
def sortksortedarray(values: list, k: int):
    result=[]
    min=[]
    heapq.heapify(min)
    value_iter = iter(values)
    for x in range(k):
        heapq.heappush(min, next(value_iter))

    while len(min) >0:
        result.append(heapq.heappop(min))
        try:
            heapq.heappush(min, next(value_iter))
        except StopIteration:
            continue
    print(result)

x = [3,-1,2,6,4,5,8]
sortksortedarray(x, 2)