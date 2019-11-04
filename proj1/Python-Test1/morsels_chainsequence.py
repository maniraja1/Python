class ChainSequence:

    def __init__(self,*args):
        self.sequences = list()
        self.length = 0
        for x in args:
            self.sequences.append(x)

    def __getitem__(self, item):
        temp=list()
        for x in self.sequences:
            for y in x:
                temp.append(y)
        if isinstance(item,slice):

            r = item.indices(self.length)
            return [temp[i] for i in range(*r)]

        else:
            return temp[item]

    def __len__(self):
        for x in self.sequences:
            self.length += len(x)
        return self.length

    def __add__(self, other):
        self.sequences.append(other)
        return self

    def __repr__(self):
        return f"ChainSequence({', '.join(repr(s) for s in self.sequences)})"





chained = ChainSequence('abcd', [1, 2, 3])

print(chained[1])
print(chained[-1])
print(chained[4])
print(len(chained))


print(chained.sequences)

x = [2, 1]
y = [3, 4]
z = [11, 18]

chained = ChainSequence(x, y, z)
print(chained.sequences)
print(chained[4], chained[5])
y.append(7)
print(chained[4], chained[5])
print(chained.sequences)
print(*chained)
print(chained[1:5])
print(chained.sequences[-1][1])
chained + 'hello'
print(*chained)
print(chained.sequences)
chained = chained + 'hello'
print(chained.sequences)
chained += (4,5, 6)
print(*chained)
chained += (4,5, 6)
print(chained.sequences)
print(chained)


'''
from collections import ChainMap
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
x = ChainMap(adjustments, baseline)
print(x)
print(x['art'])
print(x['music'])
adjustments['music']='mani'
print(x['music'])
'''

'''
 i=0
 print(item)
 print(self.length)
 for x in self.sequences:
     if item < (len(x)+i):
         return x[item-i]
     elif item > self.length:
         StopIteration
     else:
         i += len(x)'''