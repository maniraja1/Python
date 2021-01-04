
'''
Given a sorted list and an integer value k find the smallest value that is greater
than k

'''
def search_greater_than_index(array: list, val: int)->int:
    left, right = 0, len(array)-1
    result = None
    while left <= right:
        if result is None:
            middle = (left+right)//2
            if val > array[middle]:
                left = middle+1
            elif val < array[middle]:
                right=middle-1
            else:
                result=middle
        else:
            result += 1
            if array[result]>val:
                break
    print(result)

x=[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401, 401]
search_greater_than_index(x,50)




