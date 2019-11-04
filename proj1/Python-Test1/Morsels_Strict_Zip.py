
from collections.abc import Sequence
import types
from itertools import repeat, count, islice


class strict_zip:

    def __init__(self,*args):
        self.collection = list(args)
        self.count = len(self.collection)
        self.array = []
        self.counter = 0
        self.innerarray = []
        self.maxlength = 0

        self.innerarray.clear()

        for x in self.collection:
            if isinstance(x,types.GeneratorType):
                self.innerarray.clear()
                for x2 in x:
                    self.innerarray.append(x2)
                self.collection[self.counter]=self.innerarray
            self.counter += 1

        for x in self.collection:
            if isinstance(x, Sequence) and len(x)>self.maxlength:
                self.maxlength=len(x)


        self.counter = 0

    def __next__(self):
        self.array.clear()
        for x in self.collection:
            if isinstance(x, Sequence):
                try:
                    self.array.append(x[self.counter])
                except IndexError:
                    pass
            elif isinstance(x, (repeat,count)):
                self.array.append(next(x))
        if (len(self.array)) > 0 and (len(self.array)) != len(self.collection):
            raise ValueError(f'Sequences have different lengths.')
        self.counter += 1
        if len(self.array)>0:
            return tuple(self.array)
        else:
            raise StopIteration


    def __getitem__(self, item):
        self.array.clear()
        for x in self.collection:
            if isinstance(x, Sequence):
                try:
                    self.array.append(x[self.counter])
                except IndexError:
                    pass
            elif isinstance(x, (repeat,count)):
                self.array.append(next(x))
        if (len(self.array)) > 0 and (len(self.array)) != len(self.collection):
            raise ValueError(f'Sequences have different lengths.')
        self.counter += 1
        if len(self.array)>0:
            return tuple(self.array)
        else:
            raise StopIteration



for number, letter in strict_zip((1, 2, 3), 'abc'):
    print(number,letter)

for items in strict_zip([1, 2], [3, 4], [5, 6], [7, 8]):
    print(items)

'''
for letters in strict_zip('here', 'are', 'four', 'sequences'):
    print(letters)


lucas = [2, 1, 3, 4, 7, 11]
for x in (n**2 for n in lucas):
    print(x)
'''
lucas = [2, 1, 3, 4, 7, 11]
x = dict(strict_zip(lucas, (n**2 for n in lucas)))
print(x)

zipped = strict_zip(lucas, (n**2 for n in lucas))
print(next(zipped))
print(next(zipped))
print(list(zipped))

zipped = strict_zip(lucas, (n**2 for n in lucas))
print(list(zipped))

'''
zipped = strict_zip(lucas, (n**2 for n in lucas),[1,2,3])
print(next(zipped))
print(next(zipped))
print(next(zipped))
print(next(zipped))

print(next(repeat(4)))
print(next(repeat(4)))
print(type(repeat(4)))
x= [[1,2,3],repeat(4)]
print(next(x[1]))
'''


zipped = strict_zip([1,2,3],count())
print(next(zipped))
print(next(zipped))
print(next(zipped))





