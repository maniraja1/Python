from collections import UserDict
files = UserDict()
b=[1,2]
files.b = b
print(files.b)
print(b)
b.append(3)
print(files.b)
print(b)
files.b.append(5)
print(files.b)
print(b)

files['a']=b
print(files.data)

def test(*numbers, startval=0):
    total=startval
    for x in numbers:
        total += x
    print(total)
x = [1,2,3]
print(*x)
test(*x, startval=20)

x = '1,2,3'
print(x.split(","))