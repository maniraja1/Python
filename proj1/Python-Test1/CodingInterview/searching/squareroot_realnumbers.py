'''
Given a floating point number find the square root

This is similar to integer square root problem but there are some subtle differences
you cannot do the below since these are floating point numbers and depending on the
precison we don't want to make any assumptions
    right=mid-1
    left=mid+1
You instead use the below
    right=mid
    left=mid
we use math.isclose() to compare two floating point numbers
we do not use the floor value of the division but the actual floating point value

You can also pass integers to the below function and it yields accurate square root
'''

import math
def squareroot_real(k: float, precision: int = 9)->float:
    left, right=(0.0, k) if k>=1.0 else (k, 1.0)  #     not sure if we need this
    i = 1

    #while not math.isclose(left, right):
    while right-left>0.0001:
        mid = (left+right)/2
        val = mid*mid

        #print(left, right, mid)
        if val >= k:
            right = mid
        else:
            left = mid
        i += 1
    print(left,right, i)

squareroot_real(0.4)
squareroot_real(1000)

#print(math.isclose(31.622776587028056, 31.622776645235717), 31.622776587028056-31.622776645235717)
#print(math.isclose(31.622776587028056, 31.622776616131887),31.622776587028056- 31.622776616131887)

print(float('0.'+str.zfill('',3)+'1'))