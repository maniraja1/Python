'''
delete dupes from sorted array
[2,3,5,5,7,11,11,11,13] should return [2,3,5,7,11,13,0,0,0]
This below example is more efficient. Notice it does not pop elements out.
Pop has a price penalty because arrays have to be shifted when you pop elements in the middle
'''
def deletedupes2(a):
    if not a:
        return 0
    w = 1
    for i in range(1, len(a)):
        if a[w-1] != a[i]:
            a[w]=a[i]
            w += 1

    for i in range(w, len(a)):
        a[i]=0
    print(a)
print('#'*50)
l = [2,3,5,5,7,11,11,11,13]
deletedupes2(l)
'''
Write a program to remove a specific key from array and replace with -1
'''
def removekey(a,k):
    w=0
    for i in range(len(a)):
        if a[i]!=k:
            a[w]=a[i]
            '''if i != w:
                a[i]=-1'''
            w += 1
    print(a[:w])
print('#'*50)
l = [1,2,2,2,3,4,5]
removekey(l,2)

'''
write a program to remove if a key appears more than twice
'''
def removekey_n(a,k):
    d = dict()
    w=0
    for i in range(len(a)):
        d[a[i]]=d.setdefault(a[i], 0) + 1
        if d.setdefault(a[i]) <= 2:
            a[w]=a[i]
            w += 1
    print(a[:w])

print('#'*50)
l = [2,3,5,5,7,11,11,11,5,13,14]
removekey_n(l,2)


