'''
Find missing and duplicate values. WHen you have a list  1 to N nunbers. Then you can find
a single missing or duplicate number by subtracting n(n+1)/2 with the sum of numbers in the list

However if there is one duplicate and one number missing then it is tough to solve using n(n+1)/2

For this we have a couple of methods
1. XOR (space efficient) find_missing_duplicate
2. Dictionary (Time efficient) find_missing_duplicate2

In the XOR method here is the algorithm
1. XOR every element in the array (miss_xor_dup)
2. XOR all numbers from 0 to N  (miss_xor_dup)
3. when you XOR every element and numbers from 0 to N, typically the cancel each other out
only the duplicate and missing number are left behind in the output 1^1=0
4. Now differbit = miss_xor_dup ^-miss_xor_dup to get the least significant bit
5. This will give you the significant bit to look for. Now look for all  numbers where the significant
bit matches with differbit and perform XOR ideally twice and store it in mis_or_dup
6. This will result in output which will either give you the missing  or  duplicate
7. you can compare mis_or_dup with list and see if it exists. If it does then that is your missing
number and if you XOR  mis_or_dup^miss_xor_dup you get the missing number


'''


import functools
def find_missing_duplicate(array: list):

    miss_xor_dup = functools.reduce(lambda v,i: v^i[0]^i[1], enumerate(array), 0)
    print(f"miss_xor_dup: {miss_xor_dup}")
    differ_bit, mis_or_dup =  miss_xor_dup & (~(miss_xor_dup-1)),0

    for i,a in enumerate(array):

        if i & differ_bit:
            print(f"i & differbit: {i, differ_bit}")
            mis_or_dup ^= i
            print(f"mis_or_dup:  {mis_or_dup}")

        if a & differ_bit:
            print(f"a & differbit: {a, differ_bit}")
            mis_or_dup ^= a
            print(f"mis_or_dup:  {mis_or_dup}")
    print(f"mis_or_dup:  {mis_or_dup}")
    if mis_or_dup in array:
        return (mis_or_dup, mis_or_dup ^ miss_xor_dup)
    return ( mis_or_dup ^ miss_xor_dup, mis_or_dup)

x=[0,1,2,3,4,6,7,8,9,3]
#x=[5,3,0,3,1,2]
print(find_missing_duplicate(x))

def find_missing_duplicate2(array: list, n: int):
    d=dict()
    s = 0
    duplicate=None
    for x in array:
        if x not in d:
            d[x]=0
            s += x
        else:
            duplicate=x
    print(f"Duplicate: {duplicate}")
    print(f"Missing: {(n*(n+1))/2-s}")

x=[0,1,2,3,4,6,7,8,9,3]
find_missing_duplicate2(x, 9)