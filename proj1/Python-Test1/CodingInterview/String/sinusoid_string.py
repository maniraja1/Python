
def sinusoid(s):
    result = []
    for i in range(1, len(s), 4):
        if s[i]== " ":
            result.append("#")
        else:
            result.append(s[i])
    result.append('|')
    print('#'*50)
    for i in range(0, len(s), 2):
        if s[i] == " ":
            result.append("#")
        else:
            result.append(s[i])
    print('#' * 50)
    result.append('|')
    for i in range(3, len(s), 4):
        if s[i] == " ":
            result.append("#")
        else:
            result.append(s[i])
    #print(result)
    out = "  "
    i=1
    for x in result:
        if x == "|":
            print(out)
            i += 1
            if i ==2:
                out=""
            else:
                out = " "*6
        else:
            out += x
            out += " "
            if i==2:
                out += " " * 2
            else:
                out += " "*6
    print(out)


x = "hello world!"
sinusoid(x)