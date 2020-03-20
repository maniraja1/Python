
class file_looper:

    def __init__(self, filesnames, mode='r',return_exceptions=True):
        self.filenames = filesnames
        self.mode = mode
        self.return_exceptions=return_exceptions
        self._prevfilename = None
    def __iter__(self):
        try:
            for x in self.filenames:
                if self._prevfilename is not None:
                    self._prevfilename.close()
                f = open(x, self.mode)
                self._prevfilename = f
                yield f
        except FileNotFoundError:
            if self.return_exceptions:
                yield Exception("File not found")



filenames = ["file1.txt", "file2.txt", "file3.txt"]

n=1
for f in file_looper(filenames, mode="w"):
    f.write(f"File {n}!")
    n += 1

for f in file_looper(filenames):
    print(f.read())


import os, time
os.unlink("file2.txt")
for f in file_looper(filenames,'r',True):
    if isinstance(f, Exception):
        print(f)
    else:
        print(f.read())
        time.sleep(1)
