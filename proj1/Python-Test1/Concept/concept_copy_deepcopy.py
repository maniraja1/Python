'''
concept copy and deepcopy

Assignment statements in Python do not create copies of objects, they only bind names to an object.
For immutable objects, that usually doesn’t make a difference.

But for working with mutable objects or collections of mutable objects, you might be looking for a way to create
“real copies” or “clones” of these objects.

copy only copied references and deep copy actually makes another instance of the class
in copy if you change the parent class variable then  copy also reflect the change
in deep copy if you change the parent class variable then deepcopy does not reflect the change

In order to implement custom copy and deepcopy functionality you can implemenet
__copy__ and __deepcopy__

If you do not implement __copy__ then copy behaves like deepcopy
You can check this by commenting out __copy__ from below class

'''


from copy import copy, deepcopy
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = [self.x, self.y]

    def __str__(self):
        return f"Vector (x={self.x}, y={self.y}, z ={self.z})"
    '''
        if you comment the below method the copy behaves like deepcopy
        if you intend to have shallow copies working you need to define the below __copy__ method
    '''

    def __copy__(self):
        return self


v1 = Vector(x=1, y=2)
v2 = copy(v1)
v3 = deepcopy(v1)
print('#'*50)
print(f"Original: {v1}")
print(f"Copy: {v2}")
print(f"Deepcopy: {v3}")
print('#'*50)
v1.x=10
v1.z = [10,2]
print(f"Original: {v1}")
print(f"Copy: {v2}")
print(f"Deepcopy: {v3}")
print('#'*50)


xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
zs = deepcopy(xs)
print(f"Original List : {xs}")
print(f"Original List : {ys}")
print(f"Original List : {zs}")
print('#'*50)
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
zs = deepcopy(xs)
xs[1][0]=100
print(f"After Modifying first level  : {xs}")
print(f"After Modifying first level  : {ys}")
print(f"After Modifying first level  : {zs}")
print('#'*50)
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
zs = deepcopy(xs)
xs.append('new sublist')
print(f"After Modifying second level  : {xs}")
print(f"After Modifying second level  : {ys}")
print(f"After Modifying second level  : {zs}")
