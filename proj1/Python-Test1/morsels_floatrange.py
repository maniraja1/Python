from math import ceil, floor

class float_range:

    def __init__ (self, start, stop=None, step=1):

        self.start,  self.stop, self.step= start, stop, step
        self.includemax=False

        if stop is None:
            self.stop = start
            self.start=None

        if self.start is None:
            self.start = 0

        self.step = step
        self.orig_start=self.start

    def __call__(self, *args, **kwargs):
        print("Inside Call")

    def __iter__(self):
        self.start = self.orig_start
        if self.start < self.stop:
            if self.step < 0:
                return None
            if not self.includemax:
                while self.start < self.stop:
                    x = self.start
                    self.start += self.step
                    yield x
            else:
                while self.start <= self.stop:
                    x = self.start
                    self.start += self.step
                    yield x
        else:
            if self.step > 0:
                return None
            if not self.includemax:
                while self.start > self.stop:
                    x = self.start
                    self.start += self.step
                    yield x
            else:
                while self.start >= self.stop:
                    x = self.start
                    self.start += self.step
                    yield x


    def __len__(self):
        if self.start < self.stop:
            if self.step<0:
                return 0
            else:
                return int(ceil((self.stop-self.start)/self.step))
        else:
            if self.step > 0:
                return 0
            else:
                return int(ceil((self.start-self.stop)/-self.step))



    def __repr__(self):
        return f"float_range({self.start}, {self.stop}, {self.step})"

    def __reversed__(self):
        if self.start < self.stop and len(self)>0:
            return float_range(len(self)*self.step+(self.start-self.step), self.start-self.step, -self.step)
        elif self.start> self.stop and len(self)>0:
            return float_range(((len(self)*self.step)+self.start)-self.step, self.start-self.step, -self.step)
        else:
            return 0

'''
for n in float_range(0.5, 2.5, 0.5):
    print(n)

print(list(float_range(0.5, 2.5, 0.5)))

print(list(float_range(0.0, 3.0)))

print(list(float_range(3.0)))
'''
print(f"Length: {len(float_range(3.0))}")
'''
x=float_range(3.0)
print(list(x))
print(list(x))
print(list(float_range(3.5, 0, -1)))
'''
print(len(float_range(5, 10, 1.5)))
print(len(float_range(10, 5, 1.5)))
print(len(float_range(10, 5, -1.5)))
print(len(float_range(5, 10, -1.5)))
print(len(float_range(1, 11, 2)))
print(len(float_range(0.5, 7, 0.75)))
print(list(float_range(0.5, 7, 0.75)))
print(list(reversed(float_range(0.5, 7, 0.75))))

print(list(float_range(10, 5, -1.5)))
print(list(reversed(float_range(10, 5, -1.5))))

print(list(float_range(0.5, 2.5, 0.5)))
print(list(reversed(float_range(0.5, 2.5, 0.5))))

