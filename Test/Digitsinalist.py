import math
itt=3458808787
num=itt
blist=[]
i=len(str(itt))-1
while(i>=0):
    blist.append(str(num// pow(10,i)))
    num=num% pow(10,i)
    i=i-1

print(blist)

