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
