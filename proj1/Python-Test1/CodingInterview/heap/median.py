import heapq

min=[]
max=[]
heapq.heappush(max, -heapq.heappushpop(min, 0))
print(min)
print(max)
heapq.heappush(max, -heapq.heappushpop(min, 1))
print(min)
print(max)

def runningmedian(val: list):
    running_median = []
    min=[]
    max=[]

    for x in val:
        heapq.heappush(max, -heapq.heappushpop(min, x))

        if len(max)>len(min):
            heapq.heappush(min, -heapq.heappop(max))

        print(f"Min: {min}")
        print(f"Max: {max}")

        if len(min)==len(max):
            running_median.append(0.5*(min[0]-max[0]))
        else:
            running_median.append(min[0])
        print(f"Running Median: {running_median}")
    print(running_median)

x=[1, 0, 3, 5, 2, 0, 1]
runningmedian(x)    