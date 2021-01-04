
def palindrome(s):
    for x in range(len(s)//2):
        print(s[x], s[-(x + 1)])
        if s[x].lower() != s[-(x+1)].lower():
            return False
    return True
#s="malayalam"
#s="axxa"
s="Test"
print(palindrome(s))
s = "cvc1 "

def palindrome_str(s):
    i, j = 0, len(s)-1

    while i<j:

        while not s[i].isalnum():
            print("isAlnum")
            i += 1

        while not s[j].isalnum():
            j -= 1
        print(s[i], s[j])
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
        print(i, j)
    return True

#s = "Ray a Ray"
s = "Ray a Yar"
print(palindrome_str(s))

x=[1,2,3,4,5]
print(x[0])
print(x[-1])