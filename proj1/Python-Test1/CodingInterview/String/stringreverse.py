'''
3 patterns
1. Reverse string but not the words (reverse_string2)
2. reverse word but not the string (reverse_string1)
3. reverse string and also the words (reverse_string3)
'''


import string
def reverse_string1(s):
    start = 0
    reversed_str=[]
    while True:
        try:
            end = s.index(' ', start)-1
        except ValueError:
            end = len(s)-1
        print(f"Start, end: {start, end}")
        if end < 0:
           end=len(s)-1
        if start >= len(s):
            break
        print(f"Start, end: {start, end}")
        x=end
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        start = x+2
        end = 0
    print(s)


    print(reversed_str)

def reverse_string2(s):
    print(f"Original: {s}")
    s.reverse()
    print(f"Reversed: {s}")
    start = 0
    while True:
        end = (s.find(b' ', start))-1
        print(start, end)
        if end < 0:
            end = len(s)-1
        if start >= len(s):
            break
        x=end
        while start < end:
            s[start], s[end]= s[end], s[start]
            start += 1
            end -= 1

        start = x+2
        end = 0

    print(s)

def reverse_string3(s):
    start = 0
    end = len(s) - 1
    print(f"Start, end: {start, end}")
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
        print(s)
    print(s)


    print(reversed_str)

x = "Ab Quick Brown Fox"
y = list(x)
print(y)
print(y.index(' '))
y = list(y.__reversed__())
print(y)
print(y.index(' ', 0))

print("#"*50)
x = "Abcde Quickeste  Browner Fox lazy"
y = list(x)
print(f"Original String: {x}")
reverse_string1(y)
print("#"*50)
x = "Abcde Quickeste  Browner Fox lazy"
print(len(x))
y = list(x)
print(f"Original String: {x}")
reverse_string3(y)
print("#"*50)
x="abcd ef"
y=bytearray(x, 'utf-8')
print(f"Original String: {x}")
reverse_string2(y)
print("#"*50)
x = "Ab Quick Brown Fox"
y=bytearray(x, 'utf-8')
print(f"Original String: {x}")
reverse_string2(y)
print("#"*50)

