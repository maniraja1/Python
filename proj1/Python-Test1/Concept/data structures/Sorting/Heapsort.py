
def heapify(input2, indx, maxindex=None):
    if maxindex is None:
        maxindex=len(input2)-1
    x=input2[indx]
    print(f"Heapify: {input2}, {indx}, {maxindex}")
    if len(input2)-1 >= 2*indx+2 and 2*indx+2 <= maxindex:
        subarray = [x, input2[2*indx+1], input2[2*indx+2]]
        y = max(subarray)
        if y != x:
            z = subarray.index(max(subarray))
            input2[indx], input2[2*indx+z] = input2[2*indx+z],input2[indx]
            return 2 * indx + z
        else:
            return -1
    elif len(input2)-1 >= 2*indx+1 and 2*indx+1 <= maxindex:
        subarray = [x, input2[2 * indx + 1]]
        y = max(subarray)
        if y != x:
            z = subarray.index(max(subarray))
            input2[indx], input2[2 * indx + z] = input2[2 * indx + z], input2[indx]
            return 2 * indx + z
        else:
            return -1
    else:
        return -1


def heapsort(input):
    i = int((len(input) - 1) / 2)
    while i >= 0:
        x = i
        while x >= 0:
            x=heapify(input, x)
        i -= 1
    print(f"input: {input}")
    j = len(input)-1
    while j > 0:
        input[0], input[j] = input[j], input[0]
        x=0
        j -= 1
        while x>= 0:
            x=heapify(input, x, j)
            print(input,x)



input = [4,1,2,9,6,3,8,3,7,5,1]
heapsort(input)
print(input)
'''
i = int((len(input) - 1) / 2)
while i >= 0:
    x = heapify(input, i)
    print(x)
    i -= 1
print(input)
'''








