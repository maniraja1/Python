'''


Notes:
    Chain: Chain iterators together See Example 1.1
    islice
    tee: returns several independent iterators (defaults to 2) based on a single original input.
    starmap

'''


from itertools import *
from operator import *

for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i)


print('#'*20, 'islice', '#'*20)
for i in islice(count(), 5):
    print(i)
print('#'*50)
print('#'*10, 'Demo islice start and end', '#'*10)
for i in islice(count(), 5,10):
    print(i)

print('#'*20, 'tee', '#'*20)
r = islice(count(), 5)
i1, i2 = tee(r)

for i in i1:
    print ('i1:', i)
for i in i2:
    print ('i2:', i)


print('#'*50)
print('#'*10, 'Tee Demo cannot access input iterator', '#'*10)
# When you use tee you cannot use the original iterator. Doing so will affect the new iterators that are teeing off of
# the original input
r = islice(count(), 5)
i1, i2 = tee(r)

for i in r:
    print ('r:', i)
    if i > 1:
        break

for i in i1:
    print ('i1:', i)
for i in i2:
    print ('i2:', i)

print('#'*50)
print('#'*10, 'demo map', '#'*10)
# map is not part of collection but included here to show the difference between map and starmap
# use map when input iterators are not zipped together
print ('Doubles:')
for i in map(lambda x:2*x, range(5)):
    print (i)

print ('Multiples:')
for i in map(lambda x,y:(x, y, x*y), range(5), range(5,15)):
    print(i)

print('#'*50)
print('#'*10, 'demo starmap', '#'*10)
# use starmap instead of map if the arguments are already zipped as tuples
values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
for i in starmap(lambda x, y: (x, y, x*y), values):
    print(i)

print('#'*50)
print('#'*10, 'demo count', '#'*10)
for i in zip(count(1), ['a', 'b', 'c']):
    print (i)

print('#'*50)
print('#'*10, 'demo cycle', '#'*10)
j=0
for i in cycle(zip(['a','b','c'],range(1,4))):
    print(i)
    j += 1
    if j > 10:
        break

print('#'*50)
print('#'*10, 'demo repeat', '#'*10)
for i in repeat('over-and-over', 5):
    print (i)

print('#'*50)
print('#'*10, 'demo dropwhile', '#'*10)
# Returns iterator elements starting from when function returns False
def should_drop(x):
    print ('Testing:', x)
    return (x<1)

for i in dropwhile(should_drop, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print ('Yielding:', i)

print('#'*50)
print('#'*10, 'demo takewhile', '#'*10)
# Returns iterator with elements till the functions returns True
def should_take(x):
    print ('Testing:', x)
    return (x<2)

for i in takewhile(should_take, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print ('Yielding:', i)

print('#'*50)
print('#'*10, 'demo filter', '#'*10)
def check_item(x):
    print ('Testing:', x)
    return (x<1)

for i in filter(check_item, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print ('Yielding:', i)

print('#'*50)
print('#'*10, 'demo filterfalse', '#'*10)
# Returns iterator elements when filter matches condition
def check_item(x):
    print ('Testing:', x)
    return (x<1)

for i in filterfalse(check_item, [ -1, 0, 1, 2, 3, 4, 1, -2 ]):
    print ('Yielding:', i)


print('#'*50)
print('#'*10, 'demo groupby', '#'*10)
d = {'a': 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 2, "g": 3}
di = sorted(d.items(), key=itemgetter(1))
print(di)
for k, g in groupby(di, key=itemgetter(1)):
    print(k, [*map(itemgetter(0), g)])


print('#'*50)
print('#'*10, 'demo itemgetter', '#'*10)
# itemgetter returns a function that can then be used to return items from an iterator
i = ['a','b','c']
print(itemgetter(1)(i))
