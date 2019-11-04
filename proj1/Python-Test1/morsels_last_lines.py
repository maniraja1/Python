
class last_lines:

    def __init__(self,files,size=10):

        self.lines = []
        self.ctr = 1
        self.readfile(files, size)
        '''
        with open(files) as f:
            for l in f.readlines():
                self.lines.append(l)'''

    def readfile(self, files, size):
        with open(filename) as f:
            string = ''
            lists = []
            while True:
                line = f.readline(size)

                if not line:
                    if string.rstrip() != '':
                        lists.append(string)
                    lists.reverse()
                    break
                if line[-1] == '\n':
                    if string.rstrip() != '':
                        string += line
                        lists.append(string)
                    string = ''
                else:
                    string += line
        print(lists)
        while len(lists) > 0:
            if len(lists) > 0:
                ret = lists.pop(0)
                yield ret
            else:
                StopIteration

    def __next__(self):
        while self.ctr <= len(self.lines):
            self.ctr += 1
            yield self.lines[-(self.ctr-1)]


def last_lines2(filename,size=1):
    with open(filename) as f:
        string = ''
        lists = []
        while True:
            line = f.readline(size)

            if not line:
                if string.rstrip() != '':
                    lists.append(string)
                lists.reverse()
                break
            if line[-1] == '\n':
                if string.rstrip() != '':
                    string += line
                    lists.append(string)
                string = ''
            else:
                string += line
    print(lists)
    while len(lists)>0:
        if len(lists) > 0:
            ret = lists.pop(0)
            yield ret
        else:
            StopIteration

lines = last_lines('data/file.txt')
for x in next(lines):
    print(x)

lines = last_lines('data/file.txt')
print(list(next(lines)))