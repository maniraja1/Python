import weakref

class foo:
    def __init__(self):
        self.val='test'

    def __del__(self):
        print ('Deleting item')

    def store(self,value):
        self.val=value

    def show(self):
        print(self.val)


print('#############')
a=foo()
print('#############')
b=a
print('####a.show###')
a.show()
print('####b.show###')
b.show()
print('####Del A####')
del a
print('####Del B####')
del b
print('########################################')

print('#############')
a=foo()
print('#############')
b=weakref.ref(a)
print('####a.show###')
a.show()
print('####b.show###')
''' if you run b.show() it fails because of weak ref. 
You can create temporary strong reference by calling  b().show()'''
b().show()
print('####Del A####')
del a
print('####Del B####')
del b
print('#########################################')


print('#############')
a=foo()
print('#############')
''' weakref.proxy returns a strong reference but behaves like a weakref 
    when the object is deleted
'''
b=weakref.proxy(a)
print('####a.show###')
a.show()
print('####b.show###')
b.show()
print('####Del A####')
del a
print('####Del B####')
del b
print('#########################################')
