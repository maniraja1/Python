from json import loads,dumps, dump
class test:

    def __init__(self, args):
        self.processjson(args)

    def processjson(self, args):
        self.inp = loads(args)
        for key,value in self.inp.items():
            setattr(self, key, value)

    def __getitem__(self, item):
        return self.inp[item]

    def __iter__(self):
        for key, value in self.inp.items():
            yield key, value
    def __repr__(self):
        return f"{self.inp}"

    def __eq__(self, other):
        return self.inp == other

class parse:

    def __init__(self, args):
        if isinstance(args, list):
            self._obj = list()
            for x in args:
                self._obj.append(test(dumps(x)))
        else:
            self._obj = test(args)

    def __getitem__(self, item):
        if item is Ellipsis:
            print(f"item is Ellipsis: {item}")
            return self._obj
            '''
            for x in self._obj:
                return x'''
        else:
            return self._obj[item]

    def __eq__(self, other):
        return self._obj == other

    def __repr__(self):
        return f"{self._obj}"


t = """
{
    "name": "mani",
    "age": "30"
}
"""
u = """
{
    "name": "shankar",
    "age": "35"
}
"""
t2 = {'name': 'mani', 'age': '30'}

t3 = parse(t)
print(t3)
print(t3==t2)
print(t3['name'])


x = [{"id": 1, "name": "Bob"}, {"id": 2, "name": "Carol"}]
y = parse(x)
print(y)
print(y[0])
print(y[...].id)

