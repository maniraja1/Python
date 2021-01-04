from math import sqrt
def innersquare(s):
    size = int(sqrt(len(s)))
    start = size-1+2
    output = []
    for x in range(size-2):
        output.append(s[start:start+size-2])
        start += size-2+2
    return output

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(innersquare(l))