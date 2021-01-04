from math import sqrt
def getrow(s,i,revese=False):
    size = int(sqrt(len(s)))
    start = i*size-size
    if not revese:
        return s[start:start+size-1]
    else:
        return s[start+size:start:-1]

def getcolumn(s, i, reverse=False):
    size = int(sqrt(len(s)))
    start = i-1
    if not reverse:
        return s[start:len(s)-1:size]
    else:
        if start == 0:
            return s[len(s)-1-size+i:start:-size]
        else:
            return s[len(s) - 1 - size + i:start:-size]

def spiralorder(s):
    size = int(sqrt(len(s)))
    i=1
    output=[]
    subarray=s[:]
    while subarray:
        if len(subarray)==1:
            output.append(subarray)
        else:
            output.append(getrow(subarray, 1))
            output.append(getcolumn(subarray,size))
            output.append(getrow(subarray,size,True))
            output.append(getcolumn(subarray,1,True))
        i += 1
        subarray=[]
        j = size+1
        for x in range(size-2):
            subarray += s[j:j+(size-2)]
            j += (size-2)+2
        size -= 2
    print(list(y for x in output for y in x))
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
spiralorder(l)
l = [1,2,3,4,5,6,7,8,9]
spiralorder(l)
