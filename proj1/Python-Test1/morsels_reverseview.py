

class ReverseView:
    def __init__(self, lists):
        if isinstance(lists, str):
            self._input = list(lists)
        else:
            self._input = lists

    def __iter__(self):
        i = len(self._input) - 1
        while i >= 0:
            x = self._input[i]
            i -= 1
            yield x

    def append(self, val):
        self._input.insert(0,val)

    def __len__(self):
        return len(self._input)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(self.__iter__())[item]
        else:
            return list(self.__iter__())[item]

    def __str__(self):
        return f'{list(self.__iter__())}'

    def count(self, val):
        ctr = 0
        for x in self.__iter__():
            if x == val:
                ctr += 1
        return ctr

    def index(self, val):
        for idx, x in enumerate(self.__iter__()):
            if x == val:
                return idx
        raise ValueError

    def pop(self, idx=None):
        if idx is None:
            idx = 0
        else:
            idx = (-1*idx-1)
        self._input.pop(idx)


    def insert(self, indx, val):
        indx = len(self._input)-indx
        self._input.insert(indx, val)

    def extend(self, sub):
        for x in sub:
            self._input.insert(0, x)

    def __setitem__(self, key, value):
        key = len(self._input)-key-1
        self._input[key] = value








numbers = [2, 1, 3, 4, 7, 11]
reverse_numbers = ReverseView(numbers)
print(list(reverse_numbers))
print(list(reverse_numbers))
reverse_numbers.append(18)
print(list(reverse_numbers))
numbers = [2, 1, 3, 4, 7, 11]
reverse_numbers = ReverseView(numbers)
print(str(reverse_numbers))
print(reverse_numbers[0])
print(reverse_numbers[-1])
print(len(reverse_numbers))
print(reverse_numbers.append(18))
print(reverse_numbers[0])
print(len(reverse_numbers))
letters = "hi there"
view = ReverseView(letters)
print(view[-2:])
print(view[:3])
print(view[::-1])
print(list(letters))
print(view[::-1] == list(letters))
print(view.count('h'))
print(view.count('z'))
print(view.index('h'))
words = ["red", "green", "blue", "purple"]
view = ReverseView(words)
print(list(view))
print(list(words))
view.pop()
print(list(view))
print(list(words))
view.pop(0)
print(list(view))
print(list(words))
words = ["red", "green", "blue", "purple"]
view = ReverseView(words)
view.append("yellow")
print(list(view))
print(list(words))
print('#'*50)
view.insert(0, "pink")
print(list(view))
print(list(words))
numbers = [2, 1, 3, 4, 7, 11, 18]
x = [100,200]
numbers.extend(x)
print(numbers)
view = ReverseView(numbers)
view.insert(1, 14)
print(list(view))
