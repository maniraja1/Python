def ispalindrome():
    a=input('Enter a string: ')
    b=len(a)
    i=0
    for i in range(len(a)):
            if a[i]==a[-i-1]:
                print('is palindrome')
            else:
                print('is not palindrome')





ispalindrome()