A0 = dict(zip(('a','b','c','d','e','f','g'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]


A7 = {0:0,1:1}
A8 = [1,2,3]
A9 = [[0,0]]
A10 = (1,2,3,4)


print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)
print(type(A7))
print(type(A8))
print(type(A9))
print(type(A10))
