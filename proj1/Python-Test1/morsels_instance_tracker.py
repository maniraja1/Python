from weakref import WeakSet

def instance_tracker():
    """Return a new class which tracks instances of itself."""
    class TrackerMixin:
        instances = []
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            TrackerMixin.instances.append(self)
    return TrackerMixin

### Bonus1
# When you use the below function you will understand that the function is run only once not every time you instantiate the class
def instance_tracker2(attr_name='instances'):
    """Return a new class which tracks instances of itself."""
    class TrackerMixin:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            getattr(TrackerMixin, attr_name).append(self)
            print(f"InsideOfClass: {getattr(TrackerMixin, attr_name)}")
    setattr(TrackerMixin, attr_name, [])
    print(f"OutsideOfClass: {getattr(TrackerMixin, attr_name)}")
    return TrackerMixin

### Bonus2
# This will work even if the child class does not use super.__init__()
# notice we use __new__ and we have to return the object within the class.
def instance_tracker3(attr_name='instances'):
    """Return a new class which tracks instances of itself."""
    class TrackerMixin:
        def __new__(cls, *args, **kwargs):
            obj = super().__new__(cls)
            getattr(obj, attr_name).append(obj)
            return obj
    setattr(TrackerMixin, attr_name, [])
    return TrackerMixin


### Bonus3
def instance_tracker4(attr_name='instances'):
    """Return a new class which tracks instances of itself."""
    class TrackerMixin:
        def __new__(cls, *args, **kwargs):
            obj = super().__new__(cls)
            getattr(obj, attr_name).add(obj)
            return obj
    setattr(TrackerMixin, attr_name, WeakSet())
    return TrackerMixin

class Account(instance_tracker4()):
    def __init__(self, number):
        self.number = number
        super().__init__()

    def __repr__(self):
        return 'Account({!r})'.format(self.number)

print('########')
a1 = Account('4056')
print('#########')
a2 = Account('8156')


print(*Account.instances, sep='\n')


