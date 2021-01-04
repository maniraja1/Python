'''
Given a 2d sorted array. Check if a number exists
2D sorted array
    rows are no decreasing
    columns are non decreasing

Algorithm starts at first row last column and at each step it eliminates a row or column.
'''

def search2dsortedarray(array: list, k: int)->bool:
    row, column = 0, len(array[0])-1

    while row < len(array) and column>0:
        if array[row][column]==k:
            return True
        elif k > array[row][column]:
            row += 1
        else:
            column -= 1
    return False

x=[[-1, 2, 4, 4, 6],
   [1, 5, 5, 9, 21],
   [3, 6, 6, 9, 22],
   [3, 6, 8 , 10, 24],
   [6, 8, 9, 12, 25],
   [8, 10, 12, 13, 40]]
print(search2dsortedarray(x, 8))
