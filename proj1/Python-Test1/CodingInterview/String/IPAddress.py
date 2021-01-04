'''
Algorithm involves looping through the string and comparing every octet to see if its a valid IP address
There are 3 loops.
    One for the left most octet
    One for second from the left ocet
    One for the third and fourth octet
If an octet fails validation we exit the loop and go for the next iteration

Note that we deal with the last 2 octets together.
19216811
In the first iteration we would select the 3rd element(2) and the rest of the string(16811). We ignore this
In the next iteration we would select the [3:4] elements(21) and the rest of the string(6811). we ignore this
In the next iteration we would select the [3:5] elements(216) and the rest of the string(811). we ignore this

If we did 4 loops then as soon as the 4th octet fails we would have to break and move in to the next iteration
in the third octet
'''


def isvalid(s):
    return len(s)==1 or (int(s) <= 255 and s[0] != 0)

def getvalidip(s):
    out, parts = [], [None]*4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if isvalid(parts[0]):
            for j in range(i, min(len(s)-i, 4)):
                parts[1] = s[i: i+j]
                if isvalid(parts[1]):
                    for k in range(1, min(len(s)-i-j, 4)):
                        parts[2] = s[i+j:i+j+k]
                        parts[3] = s[i+j+k:]
                        if isvalid(parts[2]) and isvalid(parts[3]):
                            out.append(".".join(parts))

    print(out)


getvalidip('19216811')
x='19216811'



