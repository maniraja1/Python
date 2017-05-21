str1="python"
str2=''.join(reversed(str1))
str1=str1.split()
str1=sorted(str1)
str2=str2.split()
if(str1==str2):
    print('it\'s a palindrome')
else:
    print("it\'s not a palidrome")