'''
ROBIN KARP ALGORITHM

Searching strings within a text
The brute force algorithm requires 2 loops to compare. In python you can still do with a single loop
but then you would have to compare a list slice with the search string which can be slow

The below algorithm is called robin karp algorithm. It creates a hash for the search string
and creates a hash of the first n elements in the text, where n = len(search string)
You keep computing hash from the text by sliding one character to the right

If an hash match then you compare the lists to see if it is a real match
'''


from functools import reduce
s = "test"
t = "this is only a test"


base=26
hash_s=reduce(lambda h,c: h*base+ord(c),s,0)
hash_t=reduce(lambda h,c: h*base+ord(c), t[:len(s)], 0)

hash_power = base**max(len(s)-1, 0)

for i in range(len(s), len(t)):
    if hash_s == hash_t:
        if s == t[i-len(s):i]:
            print(f"Index: {i-len(s)}")
            break
    hash_t -= hash_power*ord(t[i-len(s)])
    hash_t = base*hash_t+ord(t[i])

if hash_s == hash_t:
    if s == t[-len(s):]:
        print(f"Index: {len(t)-len(s)}")



