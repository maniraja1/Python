from os import path
from itertools import islice
from sys import getsizeof
def splitfiles(filename, maxlines=0, maxbytes=0):


    start = 0
    file_suffix='aa'
    orig_filename, orig_file_extension = path.splitext(filename)
    while 1==1:
        counter = 0
        totalbytes = 0
        newext = orig_file_extension+'.'+file_suffix
        with open(filename, mode='r') as orig, open(path.join(orig_filename+newext), mode='w+') as nf:
            if maxlines >0:
                for line in islice(orig, start, start+maxlines):
                    nf.write(line)
                    counter += 1
                start = start + maxlines
                if counter < maxlines:
                    break
            elif maxbytes >0:
                for line in islice(orig, start,None ):
                    totalbytes += getsizeof(line)
                    if totalbytes<=maxbytes:
                        nf.write(line)
                        counter += 1
                        start += 1
                    else:
                        break
                if counter == 0:
                        break
            if file_suffix[1] == 'z':
                file_suffix = chr(ord(file_suffix[0]) + 1) + 'a'
            else:
                file_suffix = file_suffix[0] + chr(ord(file_suffix[1]) + 1)




splitfiles("data/file.txt", maxbytes=150)
