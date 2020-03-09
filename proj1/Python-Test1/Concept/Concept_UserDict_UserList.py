

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

files.setdefault('a',b)
print(files.data)
files.setdefault('a',1)
print(files.data)
files.setdefault('b',1)
print(files.data)