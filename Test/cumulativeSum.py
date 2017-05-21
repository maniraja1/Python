alist=[1,3,4,5,6,7]
sum=0
blist=[]
for i in range(len(alist)):
    sum=sum+alist[i]
    print(sum)
    blist.append(sum)

print(blist)