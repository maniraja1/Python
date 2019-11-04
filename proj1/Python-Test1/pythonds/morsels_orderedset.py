
class orderedset:

    def __init__(self,inp):
        self.set = []
        self.add(inp)

    def __getitem__(self, item):
        return self.set[item]

    def __len__(self):
        return len(self.set)

    def add (self, inp):
        if isinstance(inp, (list, tuple, dict)):
            for x in inp:
                if x not in self.set:
                    self.set.append(x)
        else:
            if inp not in self.set:
                self.set.append(inp)

    def discard (self,inp):
        if isinstance(inp, (list, tuple, dict)):
            for x in inp:
                if x  in self.set:
                    self.set.remove(x)
        else:
            if inp  in self.set:
                self.set.remove(inp)

    def __eq__(self, other):
        if isinstance(other,orderedset):
            for x,y in zip(self.set,other):
                if x != y:
                    return False
            return True

        if isinstance(other, set):
            for x in self.set:
                if x not in other:
                    return False
            return True

        return super().__eq__(other)




ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']
print(*orderedset(ordered_words))

print(*orderedset(['repeated', 'words', 'are', 'not', 'repeated']))

words = orderedset(['hello', 'hello', 'how', 'are', 'you'])

print(len(words))

print('hello' in words)

words = orderedset(['hello', 'hello', 'how', 'are', 'you'])
words.add('doing')
print(*words)

words.discard('are')
print(*words)


print(orderedset(['how', 'are', 'you']) == orderedset(['how', 'x', 'you']))
print(orderedset(['how', 'are', 'you']) == {'how', 'you', 'are'})
print(orderedset(['how', 'are', 'you']) == ['how', 'are', 'you'])

print(words[0])
print(words[-1])
'''
a = {'lion','tiger','cat','ant','zebra'}
print(a)

b = ['lion','tiger','cat','ant','zebra']
print(b)
'''

