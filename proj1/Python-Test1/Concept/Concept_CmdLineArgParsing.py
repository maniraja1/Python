'''
Quick Concept
    How to parse command line arguments in python. You have the following options
    1.sysargv
    2.getopt
    3.argparse
Module
    import argparse
Core Methods
    ArgumentParser()   -   Creates an object of type argument parser
    add_argument()     -   Add arguments to object of type Argument parser
    add_mutually_exclusive_group()    - Add mutually exclusive argument
    parse_args()       - Parse argument from object of type Argument parser
Options
    Choices
        You can pass a list of valid choice
    Action
        You can add an action to an argument
    mutually exclusive group
        you can add parameters such that both cannot be pased at the same time but at least one of them should be passed
'''
'''
Example how to use argparse.
    Save the below code and run the below command to execute from command line
        python test3.py --help
       python test3.py --a 1 --b 2 --filename "test.py" --education "highschool" --d --e --f 
    Above command cannot use positional argument, Every argument needs to be passed with argument name

'''
import argparse
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--a", default=1, help="This is the 'a' variable with a default 1")
parser.add_argument("--b", default=1, help="This is the 'b' variable with a default 1")
parser.add_argument("--filename", required=True, type=str, help="This is the 'filename' variable with a default 1")
parser.add_argument("--education",
                    choices=["highschool", "college", "university", "other"],
                    required=True, type=str, help="Your name")
parser.add_argument("--d", action="store_true", help="This is the 'D' variable")
parser.add_argument("--e", action="store_const", const=10,
                    help="This is the 'E' variable")
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('--f', action='store_true', help="This is the 'f' variable")
group.add_argument('--g', action='store_true', help="This is the 'g' variable")
args = parser.parse_args()
a = args.a
b = args.b
filename = args.filename
education = args.education
d = args.d
e = args.e
f = args.f
g = args.g
print(f"A: {a}")
print(f"B: {b}")
print(f"filename: {filename}")
print(f"education: {education}")
print(f"D: {d}")
print(f"E: {e}")
print(f"F: {f}")
print(f"G: {g}")

'''
Example sys.argv
    Parsing agrument using sys.argv
    sys.argv is a list with first element being the filename followed by the parameters. 
    You can only pass positional argument. Keyword arguments are not allowed.
'''
import sys
print(sys.argv)
print(*sys.argv[1:])