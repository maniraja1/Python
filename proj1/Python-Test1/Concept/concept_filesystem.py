'''
There are 2 modules that helps you OS module and Pathlib module
Inside the os module you have Path, walk tha help you with working with paths and searching files/folders
Inside the pathlib folder you have Path, glob, rglob that help you with paths and searches

The preferred approach is pathlib as it makes code platform independent. It automatically converts / to \
for windows even if it is hardcoded as string. see below for more details
https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/

Below are some example on how to build path and enumerate files and folders

Pathlib official documentation
https://docs.python.org/3/library/pathlib.html

'''

from pathlib import Path
# build path
x = Path('/Users/mrajagopal/Documents/git-utilitydb','UtilityDB/Utility/Table','test.txt')
print(x)
print("")
# Enumerate files recursively inside folder
x = Path('/Users/mrajagopal/Documents/git-utilitydb/UtilityDB/Utility').rglob('*.sql')
for f in x:
    print(f)
print("")
# Enumerate folders
x = Path('/Users/mrajagopal/Documents/git-utilitydb/UtilityDB/Utility').rglob('')
for f in x:
    if f.is_dir()==True:
        print(f)


