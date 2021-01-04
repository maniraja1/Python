import string

def stringToInt(x:str)->int:
    y = 0
    for i in x:
        y = y*10+string.digits.index(i)
    return y


def intToString(x:int)->str:
    c=[]
    while  x>9:
        c.append(chr(ord('0') + x % 10))
        x=x//10
    c.append(chr(ord('0') + x))
    return "".join(reversed(c))

print(stringToInt("346"))
print(intToString(467))

print(ord('0'))
print(ord('2'))