'''
This only works with a 2X2 array
For n X n array we would need to write a a more generalized form of the below algorithm
'''

from math import sqrt
def rotatearray(s):
    size = int(len(s[0]))
    for i in range(size // 2):
        for j in range(i, size - i - 1):
            s[i][j], s[j][size - 1 - i] ,s[size - 1 - i][size - 1 - j],s[size - 1 - j][i] = \
                s[size - 1 - j][i], s[i][j], s[j][size - 1 - i],s[size - 1 - i][size - 1 - j]
    print(s)




l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotatearray(l)
