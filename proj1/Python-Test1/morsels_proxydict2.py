
class ProxyDict:
    def __init__(self,data={}):
        self.data=data

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        for key, value in self.data.items():
            yield key

    def keys(self):
        x = []
        for key in self.data.keys():
            x.append(key)
        return x

    def __len__(self):
        return len([key for key in self.data.keys()])

    def items(self):
        x=[]
        for key,value in self.data.items():
            x.append((key, value))
        return x

    def values(self):
        x = []
        for value in self.data.values():
            x.append(value)
        return x

    def get(self, key, default=None):
        return {self.data.get(key,default)}

    def __repr__(self):
        return f"ProxyDict({self.data})"

    def __eq__(self, other):
        if isinstance(other, ProxyDict):
            return True if self.data == other.data else False
        elif isinstance(other, dict):
            return True if self.data == other else False
        else:
            return False



user_data = {'name': 'Trey Hunner', 'active': False}
proxy_data = ProxyDict(user_data)
print(proxy_data.keys())
print(set(proxy_data.keys()))
print(proxy_data['name'])
print(proxy_data['active'])
user_data['active'] = True
print(proxy_data['active'])
print(len(proxy_data))
print(proxy_data.items())
print(proxy_data.values())
print(proxy_data.get('name'))
print(proxy_data.get('shoe_size', 0))
print(proxy_data.get('d'))
for key in proxy_data:
    print(key)
print(proxy_data)

p1 = ProxyDict(user_data)
p2 = ProxyDict(user_data.copy())
print(p1==p2)
print(p2 == user_data)

if None == None:
    print(True)
else:
    print(False)