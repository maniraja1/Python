
from weakref import WeakSet

class Instances:
    def __init__(self):
        self.references = []
    def add(self, item):
        self.references.append(weakref.ref(item))
    def __iter__(self):
        for reference in self.references:
            item = reference()
            if item is not None:
                yield item


def track_instances(cls):
    def __init__(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        cls.instances.add(self)
    original_init = cls.__init__
    cls.instances = Instances()
    cls.__init__ = __init__
    return cls

def track_instances_complex(arg):
    def decorator(cls):
        original_init = cls.__init__
        def __init__(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            getattr(self, attr_name).add(self)
        setattr(cls, attr_name, WeakSet())
        cls.__init__ = __init__
        return cls
    if isinstance(arg, type):
        attr_name = 'instances'
        return decorator(arg)
    else:
        attr_name = arg
        return decorator

@track_instances_complex
class bankaccount:
    def __init__(self, bal):
        self.bal=bal

a=bankaccount(10)
b=bankaccount(20)

print(bankaccount.instances)
