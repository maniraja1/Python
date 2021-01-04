from collections.abc import Iterable

class running_mean:
    def __init__(self, input):
        if not isinstance(input, Iterable):
            raise Exception(ValueError("Input is not Iterable"))

        self.input = iter(input) # converts a list to iterable
        self._count = 0
        self._total = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            x = next(self.input)
            self._total += x
            self._count += 1
            return (x, self._total/self._count)
        except IndexError:
            raise StopIteration

    def send(self, value):
        try:
            x = value
            self._total += x
            self._count += 1
            return (x, self._total / self._count)
        except IndexError:
            raise StopIteration





means = running_mean([2, 4, 3, 5])
for x in means:
    print(x)

print(list(running_mean([2, -1, 2, 0])))
print(list(running_mean([10, 4, 7, 5, 2, 14])))



from itertools import count
for item, mean in running_mean(count()):
    print(item, mean)
    if item > 10:
        break

means = running_mean([4, 2, 1])
print(next(means))
print(next(means))
print(means.send(3))
print(next(means))

means = running_mean([4, 1, 2])
print(means.send(10))
print(next(means))
print(next(means))
print(next(means))
print(means.send(3))