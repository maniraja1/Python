

class Unpacker:

    def unpacker(self,dict1):
        for k in dict1.keys():
            setattr(self,k,dict1[k])

    def __init__(self,dict1):
        self.unpacker(dict1)

    def __getitem__(self, item):
        try:
            tuple_out = tuple()
            if isinstance(item, tuple):
                for i in item:
                    tuple_out = (*tuple_out, getattr(self, i))
                return tuple_out
            else:
                i = item
                return getattr(self, i)
        except KeyError as e:
            print(f"KeyError:{i}")
            raise Exception(e)
        except Exception as e:
            print(f"Exception:{e}")


    def __setitem__(self, key, value):
        if isinstance(key, tuple) and isinstance(value, tuple):
            for k, v in zip(key, value):
                print(f"Key:{k}")
                print(f"Value:{v}")
                setattr(self, k, v)
        else:
            setattr(self, key, value)

    def __str__(self):
        x = ""
        for key,value in self.__dict__.items():
            if len(x) > 0:
                x += ","
            x += f"{key}={value} "
        return f"Unpacker ({x})"


d = {'hello': 4, 'hi': 50}
u = Unpacker(d)
print(u.hello)
u.hello=5
print(u.hello)
print(u['hi'])
u.hi=10
print(u['hi'])
u['hi']=30
print(u['hi'])
print(u)
print(u['hello', 'hi'])
u['b', 'a'] = (11, 22)
print(u)
print(u['a', 'c', 'b'])
'''
from collections import OrderedDict
coordinates = OrderedDict([('x', 34), ('y', 67)])
point = Unpacker(coordinates)
x_axis, y_axis = point
print(x_axis)
'''
'''
key = {'hello': 4, 'hi': 5}
for k in key.keys():
    print(k)
    print(key[k])'''
