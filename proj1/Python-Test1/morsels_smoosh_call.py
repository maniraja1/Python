
from morsels_smoosh import * # __all__
import morsels_smoosh as x # __dir__

matrix = [1,[1, 2, 3], [4, 5, 6]]
print(list(smoosh(matrix)))

matrix = [1, 2, [3, 4], 5, 6]
print(list(smoosh(matrix)))
matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(list(smoosh(matrix)))
words = ['Python', 'is', 'lovely']
print(list(smoosh(words)))
pairs = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C')]
print(list(smoosh(pairs)))

# 2 Levels deep
matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(list(smooosh(matrix)))

#3 Levels deep
matrix = [1,2,[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(list(smoooosh(matrix)))

# 6 level deep
matrix = [1,2,[[[[[[1, 2], [3, 4]]]]]], [[5, 6], [7, 8]]]
print(list(smoooooosh(matrix)))

#7 Level deep
print(list(smooooooosh(matrix)))


#8 Level deep
matrix = [1,2,[[[[[[1, 2], [3, 4]]]]]], [[5, 6], [7, 8]]]
print(list(smoooooooosh(matrix)))


print(dir())
print(dir(x))