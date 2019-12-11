'''
Concept:
    This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in
    containers, dict, list, set, and tuple.

    namedtuple(), deque, Counter, OrderedDict, defaultdict

Module
    import collections

Notes:
        Counter: Takes an iterable and returns a dict of key and count
        See Example 1.1
        defaultdict: Creates a dict but does not give a key error. Initializes key if not exists
        see Example 1.2
        orderdeddict:same as dict but key maintains order
        see example 1.3
        deque: double ended queue used for stacks and queues
        see data structures/dequeue for more
        chainmap: strings dicts together and ouputs a list whose elements are dicts
        see Example 1.4
        namedtuple: returns a tuple with names for each position in the tuple.
        see example 1.5




'''
from collections import Counter, defaultdict, OrderedDict, ChainMap, namedtuple

# Example 1.1 Counter
print("#"*20, 'Example 1.1', '#'*20)
print("#"*20, 'Counter', '#'*20)
list1 = [1,2,3,4,1,2,2,2,2,2,6,6,8,7,3,8,1]
print(f"List1: {list1}")
list2=Counter(list1)
print(f"Counter(List1): {list2}")
print(f"Counter to list:  {list(list2.elements())}")  # returns a list containing all the elements in the Counter object.
print(f"Sort by occurrence: {list2.most_common()}")  # returns a tuple of key and count sorted by count
deduct = {1:1, 2:2}
print(f"Before Deduct: {list2}")
list2.subtract(deduct)
print(f"deduct: {deduct}")
print(f"After Deduct: {list2}")
cnt=Counter({1:3,2:4,1:6})
print(cnt)
print()

# Example 1.2 Defaultdict
print("#"*20, 'Example 1.2', '#'*20)
print("#"*20, 'DefaultDict', '#'*20)
c = defaultdict(int)
c["one"]=1
c["five"]=5
c["two"]=2
print(c)
print(f"c[three]: {c['three']}")

count = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    count[names] +=1
print(count)
count["Anna"]=4
print(count)
print()
# Example 1.3 OrderedDict
print("#"*20, 'Example 1.3', '#'*20)
print("#"*20, 'OrderedDict', '#'*20)
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)
for key, value in od.items():
    print(key, value)
print()
list = ["a","c","c","a","b","a","a","b","c"]
cnt = Counter(list)
od = OrderedDict(cnt.most_common())
for key, value in od.items():
    print(key, value)
print()
# Example 1.4 Chainmap
print("#"*20, 'Example 1.4', '#'*20)
print("#"*20, 'Chainmap', '#'*20)
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)
print(f"Access dict elements chain_map['a']:  {chain_map['a']}")
dict2['c'] = 5
print(f"Updating dict updates chain map as well: {chain_map.maps}")

print ([x for x in chain_map.keys()])
print ([x for x in chain_map.values()])

dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)
print(f"Adding new dict to chain map: {new_chain_map}")
print()
# Example 1.5 namedtuple
print("#"*20, 'Example 1.5', '#'*20)
print("#"*20, 'namedtuple', '#'*20)
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '13')
print(s1.fname)
s2 = Student._make(['Adam', 'joe', '18'])

# Create ordereddict from namedtuple
s3 = s1._asdict()
print("")
print(s1)
print(f"Creating an OrderedDict from NamedTuple: {s3}")

# change value of namedtuple using _replace()
print(s1)
s1=s1._replace(age='20')
print(s1)