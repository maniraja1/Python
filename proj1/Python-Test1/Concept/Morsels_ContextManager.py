'''
Concept
    Context managers allow you to allocate and release resources precisely when you want to.
    You can invoke a context manager using the WITH statement

Module

Method
    __enter__, __exit__
Notes



'''

# Example 1.0
from colorama import Fore
class ctxtmgr:

    def __init__(self, val):
        print(f"Open context manager from class {self.__class__.__name__}")
        self.a=val
        print(f"Self.a: {self.a}")

    def __enter__(self):
        print("Inside  Enter")
        print(f"Value of A: {self.a}")

    def __exit__(self,exc_type, exc_value, exc_traceback):
        print("Inside Exit")


with ctxtmgr(100) as manager:
    print(f"{Fore.GREEN}Hello world{Fore.RESET}")
print("Outside Context")


with ctxtmgr(200) as manager:
    print(f"{Fore.GREEN}Hello world{Fore.RESET}")
print("Outside Context")