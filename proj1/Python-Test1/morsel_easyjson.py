import json
from collections.abc import Mapping

class Jsonobject:

    def __init__(self,obj):
        self._json=obj

    def __getattr__(self, item):
        return self[item]

    def __getitem__(self, item):
        if isinstance(item, tuple):
            return Jsonobject({
                x: self._json[x]
                for x in item})
        return self._json[item]

    def __repr__(self):
        print("Repr")
        return repr(self._json)

    def __eq__(self, other):
        return self._json == other

    def keys(self):
        return self._json.keys()

def parse(json_string):
    return json.loads(json_string, object_hook=Jsonobject)

obj = parse('{"pink": false, "purple": true, "red": false}')
print(obj)
print(obj['purple'])
print(obj.pink)
print({**obj})
obj3 = parse('{"pink": false, "purple": true, "red": false}')
print(f"Object Equality test: {obj == obj3}")
print('#'*50)
print(obj['purple', 'pink'])

obj2 = parse('{"p" : {"pink": false, "purple": true, "red": false}, "q": {"pink": false, "purple": false, "red": false}}')
print(obj2.p['purple'])
print(obj2.q.pink)

print('#'*50)

class Jsonobject2(Mapping):

    def __init__(self,obj):
        self._json=obj

    def __getattr__(self, item):
        return self[item]

    def __getitem__(self, item):
        return self._json[item]

    def __iter__(self):
        return iter(self._json)

    def __len__(self):
        return len(self._json)

def parse2(json_string):
    return json.loads(json_string, object_hook=Jsonobject2)


obj = parse2('{"pink": false, "purple": true, "red": false}')
print(obj['purple'])
print(obj.pink)
print({**obj})
obj2 = parse2('{"pink": false, "purple": true, "red": false}')
print(f"Object Equality test: {obj == obj2}")
