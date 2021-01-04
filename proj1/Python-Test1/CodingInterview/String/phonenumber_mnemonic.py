'''
This is a backtracking algorithm. Start with an empty string get the first digit and the first character
associated with that digit. Then Get the next digit and the first character associated with that digit.
Add all the way upto the last digit once you reach till the end this is your first string you can append to
the output array. Now backtrack get the next character.
You need to do thsi till there are no more caharacters to append
Example 234
2=abc
3=def
4=ghi

a
ad                  ae                  af
adg -> output       aeg --> output      afg --> output
adh -> output       aeh --> output      afh --> output
adi -> output       aei --> output      afi --> output

b
bd                  be                  bf
bdg -> output       beg --> output      bfg --> output
bdh -> output       beh --> output      bfh --> output
bdi -> output       bei --> output      bfi --> output

c
cd                  ce                  cf
cdg -> output       ceg --> output      cfg --> output
cdh -> output       ceh --> output      cfh --> output
cdi -> output       cei --> output      cfi --> output
'''


def phone_nemonics(phonenumber:list):
    phone_code={0:"", 1:"", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
    output = []
    def backtrack(combination, next_digits):
        if len(next_digits)==0:
            output.append(combination)
        else:
            for x in phone_code[next_digits[0]]:
                print(combination+x, next_digits)
                backtrack(combination+x, next_digits[1:])

    comb=""
    backtrack(comb, phonenumber)
    print(output)

number=[2,3,4]
phone_nemonics(number)
x=[1]
print(x[1:])