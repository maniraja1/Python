x= [[5,10,8],[1,3,9],[0,4,6]]
steps=0
x=sorted(x, key=lambda y: sum(y))

def innersort(x):
    i=0
    for y in x:
        y=sorted(y)
        x[i]=y
        i += 1
    return x
innersort(x)

def sortinnerelements2(i,j,steps):
    a=x[i]
    b=x[j]
    while a[0] < b[-1]:
        rep = a[0]
        a[0]=b[-1]
        b[-1]=rep
        x[i]=a
        x[j]=b
        innersort(x)
        a=x[i]
        b=x[j]
        steps += 1
    return steps

max=-len(x)
s=-1
while s-1 >= max:
    steps=sortinnerelements2(s,s-1,steps)
    s=s-1
print(x)
print(steps)


