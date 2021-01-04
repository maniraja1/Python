
def search_sorted_array(array: list, val: int)->int:
    left, right,  = 0, len(array)-1,
    result = -1
    while left <= right:
        middle = ((right-left)//2)+left
        print(left, right, middle)

        if val>array[middle]:
            left = middle+1
        elif val < array[middle]:
            right = middle-1
        else:
            result = middle
            right=middle-1
    print(result)


x=[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401, 401]
search_sorted_array(x,50)
