'''
Algorithm to check sudoku validity. Only considers  elements  greater than 0.
check dupes per sub grid by using collections.counter. we can use a set or dict for that
check dupes per row, be careful on how you manipulate rowid
check dupes per column, be careful on how you manipulate columnid

'''

import collections
from math import floor
def sudokuverify(s):
    sudoku_size = 2
    loop_index = 0
    row = []
    column = []
    for x in range(len(l)):
        row.append({})
        column.append({})
    for x in s:
        if len([item for item, count in collections.Counter(x).items() if count > 1 and item >0])>0:
            print("Grid validation failed")
            return False

        for index, y in enumerate(x):
            if y>0:
                r = floor((index)/sudoku_size)+(sudoku_size*floor((loop_index)/sudoku_size))
                if y in row[r]:
                    print(row)
                    print("Row validation failed")
                    return False
                row[r][y]=0

                c = (index%sudoku_size)+(sudoku_size*(loop_index%sudoku_size))
                if y in column[c]:
                    print(column)
                    print("column validation failed")
                    return False
                column[c][y]=0

        loop_index += 1

    print(row)
    print(column)
    return True







l = [[1,2,3,4],[5,6,7,8],[5,6,7,8],[1,2,3,4]]
print(sudokuverify(l))
x=1
print((x//2)*2)
