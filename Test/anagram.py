str1="pythol"
str2="typhon"
str1=str1.split()
print(str1)
str1=sorted(str1)
print(str1)
str2=str2.split()
str2=sorted(str2)
print(str2)
if(str1==str2):
    print("it's an anagram")
else:
    print("it's not an anagram")