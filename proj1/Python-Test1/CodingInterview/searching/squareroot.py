
'''
Given an integer k find the largest integer whose square is less than k

'''

def squareroot(k: int)->int:
    left, right= 0, k
    i=1
    while left <= right:

        mid=(left+right)//2
        val = mid*mid
        #print(left, right, mid, val)
        if val > k:
            right =mid-1
        else:
            left = mid+1
        i += 1
    print(left - 1, (left-1)**2, i)

    # To get the decimal part of the square root
    print((k-(left-1)**2)/((k-(left-1)**2)+((left**2)-k)))



squareroot(1000)


