
def innersort(x, TotalSteps):
    s=[]
    u=[]
    for y in x:
        for z in y:
            s.append(z)
    print(x)
    prev = None
    ctr=None
    i=0
    while ctr is None or ctr > 0:
        ctr=0
        for z in s:
            if prev is None:
                prev=z
            if z < prev:
                s[i-1]=z
                s[i]=prev
                ctr +=1
                TotalSteps += 1
            else:
                prev = z
            i += 1
        prev=None
        i=0
        if ctr > 0:
            ctr = None
    while len(s) > 0:
        u.append(s[:3])
        s = s[3:]
    print(u)
    return TotalSteps

x= [[10,8,5],[1,9,3],[6,4,0]]
TotalSteps=0
print(innersort(x, TotalSteps))
