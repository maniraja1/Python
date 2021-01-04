'''
Give a sorted array find the value/index where index is equal to value.
You don't need to return all values just one of them

'''

def searchindexisequaltovalue(array: list)->int:
    left, right = 0, len(array)-1
    result = None
    while left <= len(array)-1:
        mid = (left+right)//2
        if mid < array[mid]:
            right = mid-1
        elif mid > array[mid]:
            left = mid+1
        else:
            result=mid
            break

    print(result)



x=[-2, 0, 2, 4, 6, 7, 9]
searchindexisequaltovalue(x)
