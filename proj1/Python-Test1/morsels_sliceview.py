def SliceView2(sequence, start=None, stop=None, step=1):
    """A "view" into a sequence, like a "lazy slice"."""
    start, stop, step = slice(start, stop, step).indices(len(sequence))
    minimum, maximum = 0, len(sequence)
    if step >= 0:
        maximum = min(stop, maximum)
    else:
        minimum = max(minimum, stop)
    i = start
    while minimum <= i < maximum:
        yield sequence[i]
        i += step


def SliceView3(sequence, start=None, stop=None, step=1):
    """A "view" into a sequence, like a "lazy slice"."""
    start, stop, step = slice(start, stop, step).indices(len(sequence))
    print(range(start, stop, step))
    """Implemented loop counter as a range object"""
    for i in range(start, stop, step):
        print(i)
        yield sequence[i]

class SliceView4:
    """A "view" into a sequence, like a "lazy slice"."""
    def __init__(self, sequence, start=None, stop=None, step=1):
        start, stop, step = slice(start, stop, step).indices(len(sequence))
        self.sequence = sequence
        self.range = range(start, stop, step)
        self.range_index = 0
    def __iter__(self):
        return self
    def __next__(self):
        '''when implementing next here we are keeping track of the counters manually'''
        if self.range_index >= len(self.range):
            raise StopIteration
        i = self.range[self.range_index]
        self.range_index += 1
        return self.sequence[i]

class SliceView5:
    """A "view" into a sequence, like a "lazy slice"."""
    def __init__(self, sequence, start=None, stop=None, step=None):
        self.sequence = sequence
        self.slice = slice(start, stop, step)
    def __iter__(self):
        '''Two things happen here one we are return an iterator from within the iter, so __next__ is not required
           we are not managing the iterator index but instead use range
        '''
        start, stop, step = self.slice.indices(len(self.sequence))
        for i in range(start, stop, step):
            yield self.sequence[i]

class SliceView6:
    """A "view" into a sequence, like a "lazy slice"."""
    def __init__(self, sequence, start=None, stop=None, step=None):
        start, stop, step = slice(start, stop, step).indices(len(sequence))
        '''we are creating a range object which we will use to compute the len and also use when returning iterator'''
        self.range = range(start, stop, step)
        self.sequence = sequence
    def __len__(self):
        return len(self.range)
    def __iter__(self):
        for i in self.range:
            yield self.sequence[i]

colors = ['red', 'purple', 'pink', 'blue', 'green', 'black']
print(colors[0:3])
x=list(SliceView4(colors, stop=3))
print(len(x))
print(list(SliceView3(colors, start=-2)))
print(list(SliceView3(colors,  step=2)))
y = SliceView6(colors,  step=2)
print(list(y))
print (len(y))
z = SliceView4(colors,  step=2)
print(list(z))
##print(len(z))