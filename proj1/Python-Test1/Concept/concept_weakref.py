'''
Concept
    Weak references to objects such that if the original object is deleted and if there are no additional reference
    then the object is not garbage collected

    Python garbage collection
    https://stackabuse.com/basics-of-memory-management-in-python/

Modules
    weakref

'''


import weakref

class Test:

    def __init__(self):
        pass


t1 = Test()
t2 = Test()
print(f"Creating object t1: {t1}, t2: {t2}")
print()
print("Add weak reference to object t1")
print()
x=weakref.ref(t1)
print("Add strong reference to object t2")
print()
y=t2
print(x)
print()
print(y)
print()
print("Deleting object t1, t2")
print()
del t1
del t2
print(f"Weak Ref allows object to garbage collected: {x}")
print()
print(f"Strong ref prevents object from being garbage collected: {y}")
del x
del y
print()
print('##########################################################################################')

t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()
print()
print(f"Creating object t1: {t1}, t2: {t2}, t3:{t3}, t4: {t4}")
print()
print("Create a weakset add ref to t1, t2")
print()
c = weakref.WeakSet()
c.add(t1)
c.add(t2)
print("Create a list d  with strong ref to t3, t4")
print()
d=[t3,t4]
print(c.data)
print()
print(d)
print()

del t1
del t2
del t3
del t4

print(f"Weakset allows object to be garbage collected: {c.data}")
print()
print(f"Strong ref prevents object from being garbage collected: {d}")








