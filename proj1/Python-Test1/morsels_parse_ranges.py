class parse_ranges:
    def __init__ (self, ranges):
        self.ranges = list(r.split("-") for r in ranges.split(","))
        self.intermediate = []
        self.out=[]
        self.ctr = 0
        self.length = 0
        self.elementlengths=[]
        self.prevlength = 0
        for x in self.ranges:
            try:
                start = int(x[0])
            except IndexError:
                start = 0
            try:
                end = int(x[1])
            except IndexError:
                end = start
            except ValueError:
                end = start
            for y in [range(start, end+1)]:
                self.intermediate.append(y)

    def __len__(self):
        for x in self.intermediate:
            self.length += len(x)
            self.elementlengths.append(len(x))
        return self.length

    def flatten(self):
        if len(self.out) > 0:
            return
        for x in [*self.intermediate]:
            for y in [*x]:
                self.out.append(y)

    def __next__(self):
        if self.ctr < len(self):
            for index, x in enumerate(self.intermediate):
                if index>0:
                    l = len(x)+sum(self.elementlengths[:index])
                else:
                    l=len(x)
                if self.ctr < l:
                    self.ctr += 1
                    if index>0:
                        i = self.ctr-1-sum(self.elementlengths[:index])
                    else:
                        i=self.ctr-1
                    return [*x][i]
                else:
                    self.prevlength=len(x)


    def __getitem__(self, item):
        if len(self.out) == 0:
            self.flatten()
        return self.out[item]




numbers=parse_ranges('1-2,4-4,8-10')
print(list(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

print(*parse_ranges('0-0, 4-8, 20, 43-45'))
##print(len(parse_ranges('0-0, 4-8, 20, 43-45')))
numbers = parse_ranges('100-10000')
print(len(numbers))
print(next(numbers))
print(next(numbers))
print(list(parse_ranges('0,4-8,20,43-45')))
print(list(parse_ranges('0, 4-8, 20->exit, 43-45')))
