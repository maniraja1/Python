'''
Algorithm moves from right to left.
It starts at s[-2] all the way upto S[0]
AT each step it looks at the element to its right
if s[i]<s[i+1] then subtract s[i] from value
if s[i]>s[i+1] then add s[i] and value

Notice we don't enumerate reversed(s) or s[-1::-1] but we enumerate reversed(range(len(s)-1))
This is because this will return range(2,1,0)
and it is easy to compare s[i] and s[i+1]

'''

from functools import reduce
def roman_to_integer(s):
    T = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return reduce(
        lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i-1]] else T[s[i]]),
        reversed(range(len(s)-1)), T[s[-1]]
    )

def roman_to_integer2(s):
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = T[s[-1]]
    for i in reversed(range(len(s)-1)):
        if i == len(s)-1:
            val += T[x]
        else:
            val += -T[s[i]] if T[s[i]]<T[s[i+1]] else T[s[i]]
    return val

x = 'LIX'
print(roman_to_integer(x))
print(roman_to_integer2(x))

x = 'IC'
print(roman_to_integer(x))
print(roman_to_integer2(x))


x = 'XXXV'
print(roman_to_integer(x))
print(roman_to_integer2(x))