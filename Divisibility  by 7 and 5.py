l=[]
for n in range(2000,3201):
    if (n%7==0 and n%5>0):
        l.append(str(n))
print(','.join(l))