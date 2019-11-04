
from collections import ChainMap

class ProxyDict:
    def __init__(self,*args):
        self.proxy_dict = args
        self.key=[]
        self.value=[]
        self.item=[]
        self.ctr=0
        self.maps = args

    @property
    def proxy_dict(self):
        return self._proxy_dict

    @proxy_dict.setter
    def proxy_dict(self,orig_dict):
        self._proxy_dict = ChainMap(*orig_dict)

    @property
    def maps(self):
        return self._maps

    @maps.setter
    def maps(self,val):
        self._maps = [*val]

    def keys(self):
        for k in self.proxy_dict.keys():
            self.key.append(k)
        return self.key

    def values(self):
        for v in self.proxy_dict.values():
            self.value.append(v)
        return self.value

    def items(self):
        for k,v in self.proxy_dict.items():
            self.item.append((k,v))
        return self.item

    def __getitem__(self, item):
        if self.proxy_dict[item] is None:
            raise KeyError()
        return self.proxy_dict[item]

    def __iter__(self):
        self.ctr=0
        return self

    def __next__(self):
        if self.ctr < len(self.key):
            x = self.key[self.ctr]
            self.ctr += 1
            return x
        else:
            raise StopIteration

    def get(self,item,default=None):
        if item not in self.proxy_dict.keys():
            return default
        else:
            return self.proxy_dict[item]

    def __eq__(self, other):
        if self.proxy_dict == other.proxy_dict:
            return True
        else:
            return False

    def __len__(self):
        return len(self.key)






user_data = {'name': 'Trey Hunner', 'active': False}
proxy_data = ProxyDict(user_data)
print(proxy_data.keys())
print(proxy_data['name'])
print(proxy_data['active'])
user_data['active'] = True
print(proxy_data['active'])
user_data['active'] = False
print(proxy_data['active'])
#proxy_data['active'] = False
p1 = ProxyDict(user_data)
p2 = ProxyDict(user_data.copy())
print(proxy_data==p1)
print(proxy_data==p2)
print(p2==p1)
print(len(proxy_data))
for key in proxy_data:
    print(key)
print(proxy_data.items())
print(proxy_data.values())
print(proxy_data.get('shoe_size', 0))
user_data = {'name': 'Trey Hunner', 'active': False}
site_data = {'name': 'Python Morsels', 'last_updated': 1995}
proxy_data = ProxyDict(user_data, site_data)
print(proxy_data['name'])
print(proxy_data['active'])
print(proxy_data['last_updated'])
print(proxy_data.proxy_dict)
print(proxy_data.maps)

'''
ChainMap
MappingProxyType

'''