'''
Increment Integer list[120] to list[130]
Add 2 array elements

'''

def increment(A):
    for x in reversed(range(len(A))):
        if A[x] +1 == 10:
            A[x]=0
        else:
            A[x]=A[x]+1
            break
    print(A)

increment([129])
increment([122])

def addarrays_outer(A,B):

    if len(A) > len(B):
        addarrays_inner(B,A)
    else:
        addarrays_inner(A,B)

def addarrays_inner(A,B):
    carry = 0
    for x in reversed(range(len(B))):
        try:
            z = A[x]
        except IndexError:
            z=0
        y = B[x]+z+carry
        if y > 9:
            if x>0:
                B[x]= y%10
                carry = 1
            else:
                B[x]=y%10
                B.insert(0,int(y/10))
        else:
            B[x] = y
            carry = 0
    print(B)

addarrays_outer([6,2,9],[5,5,9,6,7])
