from itertools import islice
import heapq
def streams_k(stream: list, k: int)->list:
    x=[(len(y),y) for y in stream[0:k]]
    heapq.heapify(x)
    print(x[0][0])
    for v in stream[k:]:
        print(x, (len(v), v))
        if len(v)>x[0][0]:
            heapq.heappushpop(x, (len(v), v))
    return x

x=["A", "fox", "jumped", "over", "the", "lazy", "dogs", "quick", "brown"]
print(streams_k(x,3))

