import math
def divide (seq,n,length=0,fill=0):
    pos =0
    max=0
    sublist = []
    input =[]
    temp = []
    i=0

    try:
        seqlen = len(seq)
    except TypeError:
        seqlen = length
    print(f"Length:{seqlen}")

    for x in seq:
        input.append(x)
    y = seqlen%n

    while(i<y):
        input.append(fill)
        i += 1

    while (seqlen-1 >= pos):
        max=math.ceil(seqlen/n)+pos
        sublist.append(input[pos:max])
        pos = max
    yield (sublist)


print(divide([1, 2, 3, 4, 5,6,7,8,9,1], n=3))

for section in divide([1, 2, 3, 4, 5], n=2):
    print(*section)
for section in divide(range(22), 6):
    print(tuple(section))

sections = divide([1, 2, 3, 4, 5], n=2)
print(tuple(next(sections)))

squares = (n**2 for n in range(6))
for section in divide(squares, 3, length=6):
    print(*section)

def divide_morsel2(sequence, n):
    """Return sequence by dividing sequence into n parts."""
    count = len(sequence) // n
    remainder = len(sequence) % n
    print(count)
    print(remainder)

    if count == 0:
        print([(x,) for x in sequence] + [()] * (n-remainder))
        return [(x,) for x in sequence] + [()] * (n-remainder)
    divisions = []
    start = 0
    end = count
    while start < len(sequence):
        print(f"Start:{start}")
        print(f"End:{end}")
        if remainder > 0:
            remainder -= 1
            end += 1
        divisions.append(sequence[start:end])
        start = end
        end = end + count
    return divisions

def divide_morsel3(sequence, n):
    """Return sequence by dividing sequence into n parts."""
    count, remainder = divmod(len(sequence), n)
    start, end = 0, count
    divisions = []
    for i in range(n):
        if i < remainder:
            end += 1
        divisions.append(sequence[start:end])
        start, end = end, end+count
    return divisions

def divide_morsels4(sequence, n):
    """Return sequence by dividing sequence into n parts."""
    count, remainder = divmod(len(sequence), n)
    start, end = 0, count
    for i in range(n):
        if i < remainder:
            end += 1
        yield sequence[start:end]
        start, end = end, end+count

from itertools import islice

def divide_morsel5(iterable, n, *, length=None):
    """Returns a iterable by dividing iterable into n parts"""
    if length is None: length = len(iterable)
    iterator = iter(iterable)
    count, remainder = divmod(length, n)
    for i in range(n):
        yield islice(iterator, count+(i<remainder))

from itertools import chain,repeat
NO_FILL=object()

def divide_morsel6(iterable, n, *, length=None, fill=NO_FILL):
    """Returns a iterable by dividing iterable into n parts"""
    if length is None: length = len(iterable)
    count, remainder = divmod(length, n)
    iterator = iter(iterable)
    print(f"Count:{count}")
    print(f"Remainder:{remainder}")
    if fill is not NO_FILL and remainder > 0:
        print("test")
        iterator = chain(iterator, repeat(fill))
        remainder = count+1-remainder
    if fill is not NO_FILL and count == 0:
        iterator = chain(iterator, repeat(fill))
        remainder = n
    print(f"Remainder:{remainder}")
    '''
    comment out this code to understand how repeat works
    for i in iterator:
        print(i)
    '''
    for i in range(n):
        print(f"I:{i}")
        print(i<remainder)
        yield islice(iterator, count+(i < remainder))

print('###########################')

for section in divide_morsel6([1, 2, 3, 4, 5], n=8,fill=-1):
    print(*section)

for section in divide_morsel6([1, 2, 3, 4, 5], n=2,fill=-1):
    print(*section)

for section in divide_morsel6([1, 2, 3, 4, 5,6], n=2,fill=-1):
    print(*section)

for section in divide_morsel6([1, 2, 3, 4, 5,6,7,8,9,10], n=3,fill=-1):
    print(*section)