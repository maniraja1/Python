


def mergesort(input, p=None, q=None):
    if p is None:
        p = 0
    if q is None:
        q = len(input)-1

    if q > p:
        r = int((p+q)/2)
        mergesort(input, p,r)
        mergesort(input,r+1,q)
        merge(input, p, q, r)
    return input


def merge(input, p, q, r):
    i, j=p, r+1
    for x in input[r+1:q+1]:
        for y in input[i:q+1]:
            if x<y:
                input.insert(i,x)
                input.pop(j+1)
                break
            i += 1
        j += 1


input = [4,1,2,9,6,3,8,3,7,5,1]
print(mergesort(input))