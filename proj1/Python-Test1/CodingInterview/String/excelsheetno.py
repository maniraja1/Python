from math import pow
def excelColumToInt(s):
    y=0
    for i,x in enumerate(reversed(s.upper())):
        if i == 0:
            y = ord(x)-64
        else:
            y += pow(26, i)*(ord(x)-64)
    print(f"{s}: {int(y)}")

def excelIntToColumn(s):
    x=[]
    orig = s
    while s>26:
        q,r = s//26, s%26
        if r == 0:
            q -= 1
            r = 26
        x.append(chr(64+r))
        s = q
    x.append(chr(64+s))
    print(f"{orig}:"+"".join(reversed(x)))

excelColumToInt('A')
excelColumToInt('AA')
excelColumToInt('AZ')
excelColumToInt('ZZ')
excelColumToInt('AAA')
excelColumToInt('ZZZ')
excelColumToInt('BD')

excelIntToColumn(56)
excelIntToColumn(702)
excelIntToColumn(703)
excelIntToColumn(18278)
excelIntToColumn(1)
excelIntToColumn(27)
excelIntToColumn(52)

