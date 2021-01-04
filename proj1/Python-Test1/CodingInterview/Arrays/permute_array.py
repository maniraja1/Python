'''
Algorithm permute an array A with another array P. Array P defines the new order
You should do this permutation without creating a new array and also modify the original array in place

'''
def permute2(A, P):
    for i in range(len(P)):
        if i != P[i]:
            if P[i] >= i:
                A[i], P[i]=A[P[i]], A[i]
            else:
                A[i], P[i] = P[P[i]], A[i]

    print(A)
    print(P)

A = [5, 6, 7, 8]
P = [1,3 ,2, 0]
print(A)
print(P)
print('-'*50)
permute2(A, P)

print('#'*50)
A = [5, 6, 7, 8]
P = [1,2 ,3, 0]
print(A)
print(P)
print('-'*50)
permute2(A, P)

print('#'*50)
A = [5, 6, 7, 8]
P = [3,1 ,2, 0]
print(A)
print(P)
print('-'*50)
permute2(A, P)

print('#'*50)
A = [5, 6, 7, -8]
P = [3,1 ,2, 0]
print(A)
print(P)
print('-'*50)
permute2(A, P)



print('#'*50)
A = [-5, -6, -7, -8]
P = [3,0 ,2, 1]
print(A)
print(P)
print('-'*50)
permute2(A, P)

