'''
class rawinput:
    def __init__(self):
        self.s = ""

    def getinput(self):
        self.s = input()

    def showoutput(self):
        print(self.s)

a = rawinput()
a.getinput()
a.showoutput()
'''
import math
class formula:
    def __init__(self,lst):
        C = 50
        H = 30
        self.Q = list()
        for l in lst:
            self.D=l
            var = int(math.sqrt((2 * C * self.D)/H))
            self.Q.append(var)

    def __iter__(self):
        yield from self.Q

a = formula([100,150,180])
for x in a:
    print(x)
