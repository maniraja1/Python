
def int_roman(num, deb=False):
    d = {}
    d[1000] = "M"
    d[900] = "CM"
    d[500] = "D"
    d[400] = "CD"
    d[100] = 'C'
    d[90] = 'XC'
    d[50] = 'L'
    d[40] = 'XL'
    d[10] = 'X'
    d[9] = 'IX'
    d[5] = 'V'
    d[4] = 'IV'
    d[1] = 'I'

    roman = []

    for k, v in d.items():
        x,y = divmod(num,k)
        if deb:
            print('###############')
            print(num, k, x, y)
            print('###############')
        if x>0:
            roman.append(d.get(k) * x)
        num -= k*x
        if num < 0:
            break

    return ''.join(roman)


def roman_int(roman, deb=False):
    integer=0
    twodigit=[]
    i=0
    d = {}
    d["M"] = 1000
    d["CM"] = 900
    d["D"] = 500
    d["CD"] = 400
    d["C"] = 100
    d["XC"] = 90
    d["L"] = 50
    d["XL"] = 40
    d["X"] = 10
    d["IX"] = 9
    d["V"] = 5
    d["IV"] = 4
    d["I"] = 1

    while i < len(roman)-1:
        val = roman[i:]
        searchstring = val[:2]
        if deb:
            print(roman)
            print(i)
            print(f"Val:{val}")
            print(searchstring)
        if searchstring in ("CM","CD", "XC", "XL", "IX", "IV"):
            twodigit.append(searchstring)
            roman = roman.replace(searchstring,"",1)
        else:
            i+=1

    for i in roman:
        integer += int(d.get(i))

    for i in twodigit:
        integer += int(d.get(i))

    return integer


num=1999
print(int_roman(num))

num='MCMXCIX'
print(roman_int(num))


