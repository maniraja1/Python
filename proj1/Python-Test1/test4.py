'''
from array import array
l=[1,2,3,4]
print(l)
# m = array("i", l)
m=array('i',l)
print(m)
m.append(8)
for i in m:
    print(i)

s = 'python'
t = bytearray(s,'utf-8')
print(t)
for x in t:
    print(chr(x))
    print(ord(chr(x)))
    print(x)
'''

'''
from itertools import islice
from collections import deque
l =[10,20,30,50]
y = iter(l)

print(l)
print(y)
for n in y:
    print(n)

x=zip(range(10),l)
for _, n in x:
    print(_,n)


d=deque()
y = iter(l)
for n in y:
    d.append(n)
print(d)
print(d[1])

y = iter(l)
z=islice(y, 2)
for n in z:
    print(n)

y = iter(l)
z=islice(y, 2)
print(z)
d=deque()
d.extend(islice(y, 2))
print(d)
print(d[1])
'''


