from collections.abc import Iterable
from collections import namedtuple

class FancyReader:
    def __init__(self, Lines, delimiter,fieldname=None):
        self.rows = Lines
        self.loop = 0
        self.delimiter = delimiter
        self.outdict = None
        self.fieldnames = fieldname


    @property
    def fieldnames(self):
        return self._fieldnames

    @fieldnames.setter
    def fieldnames(self, fieldname):
        if fieldname is None:
            self._fieldnames = self.rows[self.loop].split(self.delimiter)
            self.loop += 1
        else:
            self._fieldnames = fieldname

    def __next__(self):
        if isinstance(self.rows,Iterable):
            if (len(self.rows) > self.loop):
                if self.outdict is None:
                    self.outdict = namedtuple('row', self.fieldnames)
                x = self.outdict(*self.rows[self.loop].split(self.delimiter))
                self.loop += 1
                return x
            else:
                raise StopIteration

    def __iter__(self):
        return self

lines = ['w1|w2|w3', 'my|fake|file', 'has|two|rows']
reader = FancyReader(lines, delimiter='|')
print(reader.fieldnames)
for row in reader:
    print(*row)
reader = FancyReader(lines, delimiter='|',fieldname=['x','y','z'])
print(reader.fieldnames)
print(*next(reader))
print(*next(reader))
print(*next(reader))

'''
__Next__ & __iter__ were used  to create an iterator
when creating property if you dont have a setter and only define a property then you need to access the property inside init using a single underscore
when you create property and setter then you can access property without the single underscore
when you have non private attributes remember that your getter and setter should access attribute using single underscore



'''