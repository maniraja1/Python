from itertools import islice
class CyclicList:
    def loopover(self):
        while 1 == 1:
            for val in self.val1:
                print(val)
                yield val

    def __init__(self, lists):
        self.val1 = lists
    def __iter__(self):
        return self.loopover()
    def __getitem__(self, item):
        return self.val1[item]
    def __len__(self):
        return len(self.val1)
    def append(self,new):
        self.val1=self.val1+[new]
    def pop(self,index=None):
        if index == None:
            val=self.val1[len(self.val1)-1]
            del self.val1[len(self.val1)-1]
            return val
        else:
            val = self.val1[index]
            del self.val1[index]
            return val


my_list = CyclicList([1, 2, 3])

'''for x2 in my_list:print(x2)'''

print(len(my_list))
my_list.append(4)
print(len(my_list))
print(my_list.pop())
print(len(my_list))
print(my_list[1])
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[-1])
print(my_list[-3])
print(my_list[1:])
for i in range(10):
    my_list.append(i)
print(len(my_list))
print(my_list[1:])
'''
def CyclicList(iterable):
    while 1 == 1:
        for i in iterable:
            yield i


my_list = CyclicList([1, 2, 3])
for i,x2 in enumerate(my_list):
        print(x2)
'''

