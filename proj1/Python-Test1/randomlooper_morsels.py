import random
from random import shuffle
class RandomLooper:

    def __new__(cls,*args):
        outlist=[]
        for inner in args:
            for t in inner:
                outlist.append(t)
        return sorted(outlist, key=lambda k:random.random())

    def __len__(self):
        return len(self.outlist)


def RandomLooper_solution1(iterable):
    '''Since we are returning a list we can also use this to get the length'''
    items = list(iterable)
    shuffle(items)
    return items

def shuffled(iterable):
    """Return a list of the given items, in shuffled order."""
    items = list(iterable)
    shuffle(items)
    return items


def RandomLooper_solution2(iterable):
    for item in shuffled(iterable):
        yield item


class RandomLooper_Solution3:
    def __init__(self, iterable):
        self.items = shuffled(iterable)
    def __iter__(self):
        yield from self.items
    def __len__(self):
        return len(self.items)

def shuffled2(*iterables):
    items = list(chain.from_iterable(iterables))
    shuffle(items)
    return items


class RandomLooper_solution4:
    def __init__(self, *iterables):
        self.items = shuffled(*iterables)
    def __iter__(self):
        yield from self.items
    def __len__(self):
        return len(self.items)


def RandomLooper_solution5(*iterables):
    items = [
        item
        for iterable in iterables
        for item in iterable
    ]
    shuffle(items)
    return items


class RandomLooper_solution6:
    def __init__(self, *iterables):
        self.items = list(chain.from_iterable(iterables))
    def __iter__(self):
        shuffle(self.items)
        yield from self.items
    def __len__(self):
        return len(self.items)


colors = ["red", "blue", "green", "purple"]
shapes = ["square", "circle", "triangle", "octagon"]
for color in RandomLooper(colors,shapes):
    print(color)
print(len(RandomLooper(colors, shapes)))

'''
Key Takeaway is
1. You can use __New__ to Instantiate and return a object from a class
2. You can use __init__ and __Iter__ to instantiate and rerun an iterable from a class
3. Any time you create a functionn that returns a list the length function does not have to be implemented. 
In other words if you need to implement a length function you dont need a class a function that returns list will do.
4. Shuffle modified in inplace after which you can retun the list in case you wanted to shuffle the list and return.
So this has to be a 2 step process
'''