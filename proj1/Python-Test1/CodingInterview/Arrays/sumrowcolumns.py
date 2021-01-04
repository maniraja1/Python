from math import sqrt, floor
def arraysum(s):
    size = sqrt(len(s))
    row = {}
    column = {}
    for index,v in enumerate(s):
        r = floor(index//size)
        row[r]=dict.setdefault(row, r,0)+v

        c = int(index%size)
        column[c] = dict.setdefault(column, c, 0) + v

    print(row)
    print(column)

l = [1,2,3,4,5,6,7,8,9]
arraysum(l)