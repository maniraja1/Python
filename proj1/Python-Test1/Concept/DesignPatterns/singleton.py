'''
Concept
    The singleton pattern is used when there can only be one instance of a class.
    This is typically used when you design something like a task manager or concurrent access to shared resource


'''
class singleton:
    _instance = None

    def __new__(self, *args, **kwargs):
        if singleton._instance is None:
            singleton._instance = super().__new__(self)
        return singleton._instance

    def __init__(self, x):
        self.val = x
        print(self.val)


s1=singleton(x=2)
s2=singleton(x=3)

print(id(s1))
print(id(s2))
print(s1.val)
print(s2.val)