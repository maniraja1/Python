'''
Design a program that takes input size k and reads packets continuously maintaining a
uniform random subset of size k of the read packets

Algorithm, we select the first k elements loop through the list and randomly select a number x between 0 and m
and if it is less than k replace this with the current element
'''

from random import randint
def sampling(input, k):
    out = input[:k]
    m = k

    for x in input:
        m += 1
        idx = randint(0, m)
        if idx <k:
            out[idx]=x
    return out

print(sampling([1,2,3,4,5,6,7,8,9], 3))
print(sampling([1,2,3,4,5,6,7,8,9], 7))
