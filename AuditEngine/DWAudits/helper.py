from os import path
import subprocess
import time



class AuditQuery:

    def __init__(self, filename, debug=False):
        self.allowed_types = {"py"}
        self.filename = filename
        self._debug=debug


    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        if path.exists(value):
            self.__filename = value
        else:
            raise FileNotFoundError

    @property
    def filetype(self):
        return path.splitext(self.__filename)[1][1:].strip().lower()



    def executefile(self):
        try:
            if self.filetype in self.allowed_types:
                if path.exists(self.filename):
                    cmd = subprocess.run(["python", f"{self.filename}"], capture_output=True)
                    temp = cmd.stdout.decode()
                    out = temp.split("\n")
                    if self._debug:
                        print(out)
                    return eval(out[-2])
                else:
                    raise FileNotFoundError
            else:
                print (f"Unknow file type {self.filetype}")
                raise ValueError(f"filetype {self.filetype}")
        except Exception as e:
            print(f"Error occurred when running file {self.filename}")
            raise




a = AuditQuery("../Query/test.py")
out = a.executefile()
print(type(out))
print(f"Out: {out}")


'''
# Should throw error
print("#"*50)
time.sleep(1)
a = AuditQuery("test.py")
'''

'''
# Should throw error
print("#"*50)
time.sleep(1)
a = AuditQuery("../Query/test.sql")
out = a.executefile()
'''




