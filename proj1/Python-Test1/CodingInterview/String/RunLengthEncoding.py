
def encoding(s):
    count, prev, out = 1, None, []
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            out.append(count)
            out.append(s[i-1])
            count = 1
    out.append(count)
    out.append(s[-1])
    print(out)

def decoding(s):
    count,char, out = 0, None, []
    for i in s:
        if isinstance(i, int):
            count=i
        elif isinstance(i, str):
            char = i
        print(count, char)
        if count > 0 and char is not None:
            out.append(char*count)
            count, char = 0, None
    print(out)

def decoding2(s):
    count,char, out = 0, None, []
    for x in s:
        if x.isdigit():
            count=int(x)
        elif x.isalpha():
            char = x
        print(count, char)
        if count > 0 and char is not None:
            out.append(char*count)
            count, char = 0, None
    print(out)



y='aaaefffg'
encoding(y)
decoding([3, 'a', 1, 'e', 3, 'f', 1, 'g'])
decoding2('3a1e3f1g')