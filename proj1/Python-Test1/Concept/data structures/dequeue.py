'''
concept:
    Returns a new deque object initialized left-to-right with data from iterable.
    If iterable is not specified, the new deque is empty.

    Deques are a generalization of stacks and queues (“deck” and is short for “double-ended queue”)

    Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the
    same O(1) performance in either direction.
    Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n)
    memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the
    underlying data representation.

    New in version 2.4.
        If maxlen is not specified or is None, deques may grow to an arbitrary length. Otherwise, the deque is bounded
        to the specified maximum length. Once a bounded length deque is full, when new items are added, a corresponding
        number of items are discarded from the opposite end. Bounded length deques provide functionality similar to the
        tail filter in Unix. They are also useful for tracking transactions and other pools of data where only the most
        recent activity is of interest.


'''


import collections
import threading
import time
import timeit

d = collections.deque('abcdefg')
print ('Deque:', d)
print ('Length:', len(d))
print ('Left end:', d[0])
print ('Right end:', d[-1])

d.remove('c')
print ('remove(c):', d)
#########################################
print('#########################################')
d = collections.deque()
d.extend('abcdefg')
print ('extend    :', d)
d.extend('hijk')
print ('extend    :', d)
d.append('lmn')
print ('append    :', d)
#########################################
print('#########################################')
# Add to the left
d = collections.deque()
d.extendleft('abcdefg')
print ('extendleft:', d)
d.extendleft('hij')
print ('extendleft:', d)
d.appendleft('klm')
print ('appendleft:', d)
#########################################
print('#########################################')
print ('From the right:')
d = collections.deque('abcdefg')
print(d)
while True:
    try:
        print (d.pop())
    except IndexError:
        break

#########################################
print('#########################################')
print ('From the left:')
d = collections.deque('abcdefg')
print(d)
while True:
    try:
        print (d.popleft())
    except IndexError:
        break

#########################################
print('#########################################')
print('Demo dequeue is thread safe')
candle = collections.deque(range(11))

def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print (f'{direction}: {next}')
            time.sleep(0.1)
    print (f'{direction } done')
    return

left = threading.Thread(target=burn, args=('Left', candle.popleft))
right = threading.Thread(target=burn, args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()
#########################################
print('#########################################')
print('Demo dequeue.rotate')

d = collections.deque(range(10))
print ('Normal        :', d)

d = collections.deque(range(10))
d.rotate(2)
print ('Right rotation:', d)

d = collections.deque(range(10))
d.rotate(-2)
print ('Left rotation :', d)

#########################################
print('#########################################')
s="""
for x in range(100000):
    l = list(range(10))
"""
print(f" List creation loop 100000 times, executing 10 times: {timeit.timeit(s, number=10)}")
s="""
import collections
for x in range(100000):
    d = collections.deque(range(10))
"""
print(f" deque creation loop 100000 times, executing 10 times: {timeit.timeit(s, number=10)}")

s = """
l = list(range(10)) 
for x in range(100000):
    l.append(100)
"""
print(f" list append loop 100000 times, executing 10 times: {timeit.timeit(s, number=10)}")

s="""
import collections
d = collections.deque(range(10))
for x in range(100000):
    d.append(10)
"""
print(f" deque append loop 100000 times, executing 10 times: {timeit.timeit(s, number=10)}")

print('########### Performance degradation################')
s="""
l = list(range(100000))
while l:
    l.pop(0)
"""
print(f" list pop loop 100000 times, executing 10 times: {timeit.timeit(s, number=10)}")

s="""
import collections
d = collections.deque(range(100000))
while d:
    d.popleft()
"""
print(f" deque popleft loop 100000 times, executing 10 times: {timeit.timeit(s, number=10)}")

s="""
import collections
d = collections.deque(range(100000))
while d:
    d.pop()
"""
print(f" deque popright loop 100000 times, executing 10 times: {timeit.timeit(s, number=10)}")

s="""
l = list(range(1000))
for x in range(100000):
    l.insert(0,x)
"""
print(f" list insert(0,x) loop 100000 times, executing 10 times: {timeit.timeit(s, number=10)}")

s="""
import collections
d = collections.deque(range(1000))
for x in range(100000):
    d.appendleft(x)
"""
print(f" deque appendleft loop 100000 times, executing 10 times: {timeit.timeit(s, number=10)}")