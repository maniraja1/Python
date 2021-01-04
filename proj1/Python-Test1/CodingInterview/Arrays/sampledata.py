'''
Algorithm, generate a random number between 0 and len(array)-1. Replace the zeroth element with this element.
Now generate a random number between 1 and len(array)-1 and replace the first element with this element.
continue this till you have k elements.
If you have k<= n/2 the above works. If k > n/2 we should move n-k elements to the right of the list so
'''

from random import randint
def sampling(input, k):
    if k < len(input)/2:
        start = 0
        while start <=k-1:
            x = randint(start, len(input)-1)
            input[start], input[x]=input[x], input[start]
            start += 1
    else:
        start = len(input)-1
        while start >= len(input)-k:
            x = randint(0, start)
            input[start], input[x]=input[x], input[start]
            start -= 1
    return input[:k]


print(sampling([1,2,3,4,5,6,7,8,9], 3))
print(sampling([1,2,3,4,5,6,7,8,9], 7))