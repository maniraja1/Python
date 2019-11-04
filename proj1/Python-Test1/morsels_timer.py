from time import time
from statistics import mean, median, mode
class timer_morsels:

    timers = {}

    def __new__(cls, func=None,name=None):
        if name is None:
            return super().__new__(cls)
        elif name not in cls.timers:
            cls.timers[name]=super().__new__(cls)
        return cls.timers[name]

    def __init__(self, func=None,name=None):
        print(f"Name:{name}")
        print(f"Func: {func}")
        if not hasattr(self, 'running'):
            self.runs=[]
            self.splits=[]
            self.running=False
            self.namedsplits={}
        if func is not None:
            print("setting func")
            self.func = func

    def __enter__(self):
        print("Entering __enter__")
        self.start=time()
        self.running=True
        return self

    def __exit__(self,*args):
        self.elapsed = time()-self.start
        self.runs.append(self.elapsed)
        self.median = median(self.runs)
        self.mean = mean(self.runs)
        '''self.mode2 = mode(self.runs)'''
        self.min = min(self.runs)
        self.max = max(self.runs)
        self.running = False
        print("Leaving __exit__")

    def __call__(self, *args, **kwargs):
        self.__enter__()
        try:
            print("self.func")
            return self.func(*args, **kwargs)
        finally:
            self.__exit__()

    def split(self,name=None):
        if not self.running:
            raise RuntimeError("Cannot split when the parent timer is not running")
        timer2 = timer_morsels()
        if name is not None:
            timer2 = self.namedsplits.setdefault(name,timer2)
        self.splits.append(timer2)
        print("Leaving Split")
        return timer2

    def __getitem__(self, item):
        if isinstance(item,str):
            return self.namedsplits[item]
        else:
            return self.splits[item]


from time import perf_counter
class timer_morsels2:

    """Context manager to time a code block."""
    def __init__(self, func=None):
        # print(f"Name:{name}")
        print(f"Func: {func}")
        self.runs=[]
        if func is not None:
            self.func=func

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, *args):
        self.end = perf_counter()
        self.elapsed = self.end - self.start
        self.runs.append(self.elapsed)
        self.median = median(self.runs)
        ##self.mode=mode(self.runs)
        self.mean = mean(self.runs)

    def __call__(self, *args, **kwargs):
        self.__enter__()
        try:
            return self.func(*args,**kwargs)
        finally:
            return self.__exit__()





from time import sleep
with timer_morsels() as timer:
    sleep(1)

print (f"Timer.Elapsed: {timer.elapsed}")
timer = timer_morsels()
with timer:
    x = sum(range(2 ** 24))

print (timer.elapsed)
print(timer.runs)
print(x)
print('################################')
with timer:
    sum(range(2 ** 24))
    print(timer.running)
    print('X################################')
    with timer.split():
        sleep(0.5)
        print(f"test: {timer.splits}")
    print(timer.running)
    print('Y################################')
    with timer.split():
        sleep(0.7)
        print(f"test: {timer.splits}")
        print(timer.running)


print(timer.running)
print (timer.elapsed)
print(timer.runs)
print(f"timer0: {timer[0].runs}")
print(f"timer1: {timer[1].runs}")

print('###############################')
with timer_morsels(name='sleep'):
    sleep(0.2)

with timer_morsels(name='sleep') as timer:
    sleep(0.2)

    with timer.split(name='sleepdeep'):
        sleep(0.2)

    with timer.split(name='sleepdeep'):
        sleep(0.3)



with timer_morsels(name='sleep2') as t2:
    sleep(0.2)

print(timer.runs)
print(timer[0].runs)
print(timer[1].runs)
print(t2.runs)
print(timer['sleep'].runs)
for k in timer_morsels.timers:
    print(k)

print('###############################')
with timer_morsels2() as x:
    def sum_of_squares(numbers):
        return sum(n**2 for n in numbers)
    sum_of_squares(range(2**10))
    sum_of_squares(range(2**11))
    sum_of_squares(range(2**8))

print(x.runs)
print(x.median)
print(x.mean)

print('###############################')
@timer_morsels
def sum_of_squares(numbers):
    return sum(n**2 for n in numbers)
sum_of_squares(range(2**10))
sum_of_squares(range(2**11))
sum_of_squares(range(2**8))

print(sum_of_squares.runs)
print(sum_of_squares.median)
print(sum_of_squares.mean)


