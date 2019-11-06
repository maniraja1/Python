import re

'''
Special characters
    Period matches a single character except new line
    \w Alpha numeric character
    \W any character not matched by \w
    \s white space character like: space, newline, tab, return.
    \S Matches any character not part of \s (lowercase s).
    \t - Lowercase t. Matches tab.
    \n - Lowercase n. Matches newline.
    \r - Lowercase r. Matches return.
    \d - Lowercase d. Matches decimal digit 0-9.
    ^ - Caret. Matches a pattern at the start of the string.
    $ - Matches a pattern at the end of string.
    [abc] - Matches a or b or c.
    [a-zA-Z0-9] Matches any letter from (a to z) or (A to Z) or (0 to 9).
    [^0] can be used as a complement
    \A - Uppercase a. Matches only at the start of the string. Works across multiple lines as well.
    \b - Lowercase b. Matches only the beginning or end of the word.
    + - Checks for one or more characters to its left.
    * - Checks for zero or more characters to its left.
Repititions
    {x} - Repeat exactly x number of times.
    {x,} - Repeat at least x times or more.
    {x, y} - Repeat at least x times but no more than y times.
greedy 
    pattern followed by + or *
    \w+,\w* (Alphanumeric greedy search)
    .+,.*   (Except new line greedy search)
group
    
Methods
    re.search - returns a match as long as it finds a match in the string
    re.match - returns a match object only if it matches the beginning of the string
    re.findall - Finds all the possible matches in the entire sequence and returns them as a list of strings. 
    re.fullmatch - If the whole string matches the regular expression pattern, return a corresponding match object.
    re.sub(pattern, repl, string, count=0, flags=0)
    re.compile() - Compiles a regular expression pattern into a regular expression object

Reference  
    https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial#REinPython
'''

text="500000000 A quick fox 10 jumped over 2 the lazy dogs xyz@abc.com blah blah blah xxx@yyy.com"
# Alpha numeric search
print("Alphanumeric search demo")
print(re.match(r'\w+',text).group())
print(re.search(r'\w+',text).group())
print(re.findall(r'\w+',text))
print(re.fullmatch(r'.+',text).group())
print()

# Groups
print("Group search demo")
print(re.search(r'(\w+)@(\w+).com',text).group())
print(re.search(r'(\w+)@(\w+).com',text).group(1))
print(re.search(r'(\w+)@(\w+).com',text).group(2))
print()

# groups+findall
print("Group search + Findall demo")
print(re.findall(r'(\w+)(@)(\w+).com',text))
print(re.findall(r'(\w+)(@)(\w+).com',text))
print(re.findall(r'(\w+)(@)(\w+).com',text))
print()

# Matches decimal digit 0-9.
print("Number search using greedy search and repititions demo")
print(re.match(r'\d{2}',text).group())
print(re.search(r'\d+',text).group())
print(re.findall(r'\d{2}',text))
print(re.fullmatch(r'\d+\w+',text))
print()

print(re.split(r'\s',text))
print()


text = 'coooooookie'
print("Using + without a pattern looks for character in the left and checks for one or more matchC")
print(re.match(r'co+',text).group())
print()

text='colouress'
print("Using * without a pattern looks for character in the left and checks for zero or more match")
print(re.match(r'colou?',text).group())
print(re.match(r'colou?.*',text).group())
print()

text="500000000 A quick fox 10 jumped over 2 the lazy dogs xyz@abc.com"
print("Using re.sub")
print(re.sub(r'\w+@\w+.com','mani@salesforce.com',text))
print()


# compile
pattern = re.compile(r"cookie")
sequence = "Cake and cookie"
print("Using re.compile")
print(pattern.search(sequence).group())