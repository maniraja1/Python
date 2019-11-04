
from itertools import groupby
from functools import singledispatch

class natural_sort:
    def __init__(self, string, *, key=None, reverse=False):
        self.natural_key = singledispatch(self.natural_key)
        self.natural_key.register(str, self._natural_key_str)
          
        self.out=[]
        if key is None:
            key = self.natural_key
        print(f"Input string: {string}")
        self.out = sorted(string, key=key, reverse=reverse)

    def natural_key(self, string2):
        raise TypeError(f"Unknown type: {type(string2)}")

    def _natural_key_str(self, string2):
        print(f"string input to natural key func is : {string2}")
        val = []
        for k, g in groupby(string2, str.isdigit):
            if k:
                val.append((int("".join(g))))
            else:
                val.append("".join(g).casefold())
        return val

    def __getitem__(self, item):
        return self.out[item]




for x in natural_sort(['uncle', 'Yankee', 'India', 'hotel', 'zebra', 'Oscar']):
    print(x)

print ('-------------------------------')
for x in natural_sort(['uncle', 'Yankee', 'India', 'hotel', 'zebra', 'Oscar'], reverse=True):
    print(x)

print ('-------------------------------')
for x in natural_sort(['McDonald', 'MCDONALD', 'Mcdonald', 'MacDonald']):
    print(x)


def commaless(s): return s.replace(',', '')
for x in natural_sort(['Li, Bo', 'Li Smith, Sofia', 'Li Smith, An'], key=commaless):
    print(x)


for x in natural_sort([['my', 'dog'], ['my', 'cat'], ['ab', 'ant'],['my','bat']]):
    print(x)
