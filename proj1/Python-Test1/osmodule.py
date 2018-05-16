import os


### To print attribute and methods in any module
print(dir(os))

### change directory
os.chdir('/home')

### print current working directory
print(os.getcwd())

#### mkdir
## This will create a single folder and needs the parent folder to exist
os.mkdir("/Users/mrajagopal/Documents/test2/subtest")

### This will create the tree structure
os.makedirs("/Users/mrajagopal/Documents/test2/subtest")


### Remove dirs
#### Will not remove intermediate dirs
os.rmdir()

### Will remove intermediate dirs
os.removedirs()

#### rename
os.rename('orig_file','Nw_file')

###
os.stat('Filename')
os.stat('Filename'.st_mtime)


### prints dir information as you traverse the path
for dirpath in os.walk("/Users/mrajagopal/Documents"):
    print(dirpath)

### print environment variable
print(os.environ.get('HOME'))


### Join 2 file paths
print(os.path.join(os.environ.get('HOME'),'test.txt'))

### Get filename with extensio
print(os.path.basename('/Users/mrajagopal/Documents/test2/subtest/test.txt'))

### get folder path
print(os.path.dirname('/Users/mrajagopal/Documents/test2/subtest/test.txt'))

### check if path is valid
print(os.path.exists('/Users/mrajagopal/Documents/test2/subtest/test.txt'))

#### check if dir is valid dir
print(os.path.isdir('/Users/mrajagopal/Documents/test2/subtest/test.txt'))

### check if file is valid file
print(os.path.isfile('/Users/mrajagopal/Documents/test2/subtest/test.txt'))

### split the extension of a file
print(os.path.splitext('/Users/mrajagopal/Documents/test2/subtest/test.txt'))