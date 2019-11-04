from contextlib import contextmanager

class comparator:
    defaultdelta = 1e-7
    def __init__(self,val,*, delta=None):
        self.val = val
        if delta is None:
            self._delta = comparator.defaultdelta
        else:
            self._delta = delta

    def __eq__(self, other):
        if abs(self.val-other) <= self._delta:
            return True
        else:
            return False

    def __repr__(self):
        return (f"Comparator({self.val},delta={self._delta})")

    def __add__(self, other):
        if(isinstance(other,comparator)):
            delta = other.delta
            otherval = other.val
        else:
            delta = -999
            otherval = other
        return comparator(self.val + otherval, delta=self._delta if self._delta > delta else delta)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if (isinstance(other, comparator)):
            delta = other.delta
            otherval = other.val
        else:
            delta = -999
            otherval=other
        return comparator(self.val - otherval,delta=self._delta if self.delta > delta else delta)

    def __rsub__(self, other):
        return self.__sub__(other)

    @property
    def delta(self):
        return self._delta

    @delta.setter
    def delta(self,value):
        raise Exception("Cannot set value for delta")

    @contextmanager
    def default_delta(delta):
        original = comparator.delta
        comparator.defaultdelta=delta
        try:
            yield
        finally:
            comparator.delta = original


'''

target = comparator(0.12)
n = 0.1+0.02
print(n)
print(n == 0.12)
print(n == target)

target = comparator(5,delta=0.1)
print(target == 5.05)
print(target == 4.98)
print(target == 5.2)

print(target)

'''
almost_100 = comparator(100, delta=1)
almost_50 = almost_100-50
almost_110 = almost_100+10
print(almost_50)
print(almost_110)
print(109==almost_110)
print(108==almost_110)


nearly_five = comparator(5, delta=0.1)
almost_100 = comparator(100, delta=1)
almost_105 = almost_100 + nearly_five
print(almost_105)
print(f"Delta:{almost_105.delta}")
#almost_105.delta=2

with comparator.default_delta(1):
    almost_100 = comparator(100)
    print(almost_100)
    print(101, 101==almost_100)
    print(101, 102 == almost_100)





