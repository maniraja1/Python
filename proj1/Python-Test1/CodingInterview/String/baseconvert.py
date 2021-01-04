import string
def baseconvert(s, b1, b2):
    y=0
    for x in s:
        y = y*b1+string.digits.index(x)

    c=[]
    while y>b2-1:
        z = ord('0')+y%b2
        if z >57:
            z=64+(z-57)
        c.append(chr(z))
        y=y//b2
    z=ord('0')+y%b2
    if z > 57:
        z = 64 + (z - 57)
    c.append(chr(z))
    return "".join(reversed(c))

print(baseconvert('615', 7, 13))
