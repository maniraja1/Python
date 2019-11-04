from io import TextIOBase
from io import StringIO
import sys
class WriteSpy2(TextIOBase):

    """File-like object for wrapping around multiple writable files."""
    """Notice this class will behave like a context manager because it derives from TextIOBase class"""
    def __init__(self, *files, close=True):
        self.files = files
        self._close = close

    def write(self, text):
        self._checkClosed()
        for stream in self.files:
            stream.write(text)

    def writable(self):
        self._checkClosed()
        return True

    def flush(self):
        self._checkClosed()
        for stream in self.files:
            stream.flush()

    def close(self):
        if self._close:
            for stream in self.files:
                stream.close()
        super().close()

class WriteSpy3:

    """File-like object for wrapping around two writable file streams."""
    """This is a verbose version of the class"""
    """This is an example of how to implement a context manager"""
    def __init__(self, stream, spy, close=True):
        self.stream = stream
        self.spy = spy
        self._close = close
        self._closed = False

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def write(self, text):
        if self._closed:
            raise ValueError("File is closed")
        self.stream.write(text)
        self.spy.write(text)

    def writable(self):
        if self._closed:
            raise ValueError("File is closed")
        return True

    @property
    def closed(self):
        return self._closed

    def close(self):
        if self._close:
            self.stream.close()
            self.spy.close()
        self._closed = True

class stdout_spy:

    """Temporarily spy on standard output."""

    def __init__(self):
        self.captured = StringIO()

    def __enter__(self):
        self.real_stdout = sys.stdout
        sys.stdout = WriteSpy3(self.captured, sys.stdout)
        print(f"Enter: {self.captured.getvalue()}")
        return self.captured

    def __exit__(self, *args):
        sys.stdout = self.real_stdout

class readspy(TextIOBase):

    def __init__(self,stream,spy):
        self.stream = stream
        self.spy = spy

    def read(self):
        data = self.stream.read()
        print("read")
        self.spy.write(data)
        return data

    def readline(self):
        data = self.stream.readline()
        print("readline")
        self.spy.write(data)
        return data

    def readable(self):
        return True

class stdinspy:

    def __init__(self):
        self.spy=StringIO()

    def __enter__(self):
        self.stdin=sys.stdin
        sys.stdin=readspy(sys.stdin,self.spy)
        return self.spy

    def __exit__(self,*args):
        sys.stdin = self.stdin

class iospy:

    def __init__(self):
        self.fake_stdout, self.real_stdout = StringIO(), sys.stdout
        self.fake_stderr, self.real_stderr = StringIO(), sys.stderr
        self.fake_stdin, self.real_stdin = StringIO(), sys.stdin

    def __enter__(self):
        sys.stdout = WriteSpy3(self.real_stdout, self.fake_stdout, close=False)
        sys.stderr = WriteSpy3(self.real_stderr, self.fake_stderr, close=False)
        sys.stdin = readspy(self.real_stdin, self.fake_stdin)
        return self

    def __exit__(self, *args):
        sys.stdout = self.real_stdout
        sys.stderr = self.real_stderr
        sys.stdin = self.real_stdin

    @property
    def stdout(self):
        return self.fake_stdout.getvalue()

    @property
    def stderr(self):
        return self.fake_stderr.getvalue()

    @property
    def stdin(self):
        return self.fake_stdin.getvalue()
