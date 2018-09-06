import collections
from collections import  deque
from itertools import  islice,repeat,chain

def window(numbers,win,fill):
    if(isinstance(numbers, collections.Iterable)):
        print("Iterable")
        out=set()
        innerarray=[]
        while len(numbers) >= win:
            i=1
            for n in numbers:
                if(i <= win):
                    innerarray.append(n)
                    i += 1
                if(i > win ):
                    out.add(tuple(innerarray))
                    innerarray=[]
                    i=1
            if len(innerarray) > 0:
                while len(innerarray) < win :
                    innerarray += (fill,)
                out.add(tuple(innerarray))
            innerarray=[]
            numbers.remove(numbers[0])
        return sorted(out)
    else:
        print("not an iterable")


'''trey's solution'''


def window2(iterable, n,fill=None):
    """Return list of tuples of items in given iterable and next n-1 items."""
    items = []
    current = ()
    for item in iterable:
        if len(current) < n:
            current = current + (item,)
        else:
            current = current[1:] + (item,)
        if len(current) == n:
            items.append(current)
    if len(current) < n:
        '''current = current + ((fill,)*(n-len(current)))'''
        current = *current,*(fill,)*(n-len(current))
        items.append(current)
    return items


'''trey's solution tuple unpacking'''


def window3(iterable, n):
    """Return list of tuples of items in given iterable and next n-1 items."""
    items = []
    current = ()
    for item in iterable:
        if len(current) < n:
            current = (*current, item)
        else:
            current = (*current[1:], item)
        if len(current) == n:
            items.append(current)
    return items


'''trey's solution with generator as output'''


def window4(iterable, n,fill=None):
    """Return list of tuples of items in given iterable and next n-1 items."""
    items = []
    current = ()
    for item in iterable:
        if len(current) < n:
            current = (*current, item)
        else:
            current = (*current[1:], item)
        if len(current) == n:
            yield current
    if len(current) < n:
        yield current + (fill,) * (n - len(current))


''' trey's solution with dequeue solution'''


def window5(iterable, n, fill=None):
    """Yield tuples including iterable item and the next n-1 items."""
    if n == 0:
        return
    current = deque(maxlen=n)
    for item in iterable:
        current.append(item)
        if len(current) == n:
            yield tuple(current)
    if len(current) < n:
        yield tuple(current) + (fill,) * (n - len(current))

'''trey's solution dequeue and islice'''
def window6(iterable, n, fill=None):
    if n == 0:
        return
    iterator = iter(iterable)
    current = deque(islice(iterator, n), maxlen=n)
    yield tuple(current) + (fill,)*(n-len(current))
    for item in iterator:
        current.append(item)
        yield tuple(current)

'''trey's solution deque, islice, repeat, chain'''
def window7(iterable, n,fill=None):
    if n == 0:
        return
    iterator = iter(iterable)
    current = deque(islice(chain(iterator, repeat(fill)), n), maxlen=n)
    yield tuple(current)
    for item in iterator:
        current.append(item)
        yield tuple(current)


x = window7([1,2,3,4,5,6,7,8,9,10,11,12],4,-1)
for x2 in x:
    print(x2)