
def quicksort(input,low=0,high=None, side=None):
    if high is None:
        high = len(input)-1

    if side is None:
        side = 'Original'

    if low >= high:
        return

    pivot = partition(input, low, high, side)
    quicksort(input, low, pivot-1, 'left')
    quicksort(input, pivot+1, high, 'right')
    return input



def partition(input, low, high, side):
    pivot = input[high]

    i = low-1
    j = low
    movementcounter = 0
    #print(pivot, low, high, side, input)
    while j <= high:
        if input[j] < pivot and j > i:
            i += 1
            input[i], input[j] = input[j], input[i]
            movementcounter += 1
        j += 1
    input[i+1], input[high] = input[high], input[i+1]
    #print(pivot, low, high, side, movementcounter, input)
    return i+1

'''
This below code is use the median element as a pivot and this is not working as expected
def quicksort2(input,low=0,high=None, side=None):
    if high is None:
        high = len(input)-1

    if low >= high:
        return
    if side is None:
        side = 'Original'
    pivot = partition3(input, low, high, side)
    quicksort(input, low, pivot-1, 'left')
    quicksort(input, pivot+1, high, 'right')
    return input


def partition3(input, low, high, side):

    x = int((high-low)/2)
    input[x], input[high] = input[high], input[x]
    pivot = input[x]
    print(pivot, low, high, side, input)
    i = low
    j = low

    while j < high:
        if input[j] <= pivot and j > i:

            input[i], input[j] = input[j], input[i]
            i += 1
        j += 1
    input[i], input[high] = input[high], input[i]
    print(input)
    print(i)
    return i
'''
input = [4,1,2,9,6,3,8,3,7,5,1]
print(f"original input: {input}")
print("")
print(quicksort(input))
print("")
print(f"original input: {input}")
print("")
print(quicksort(input))
print("")
print(f"original input: {input}")
print("")
print(quicksort(input))
print("")


