'''
Algorithm to return a subset of k elements with equal probability from set [0,1,2,3,...n-1]
Input would be k and n

Create am empty dict
Loop from 0 to k and select a random number between x and n and if this key does not exist
in the dict add it to the dict. Add index as key and also the value as key.

'''
from random import randint
def sampling(n,k):
    occurrences = {}
    for x in range(k):
        val = randint(x, n)
        while val in occurrences.keys():
            val = randint(x, n)
        occurrences[x]=val
        occurrences[val]=x
    return [occurrences[i] for i in occurrences.keys() if i < k]



print(sampling(100,3))

