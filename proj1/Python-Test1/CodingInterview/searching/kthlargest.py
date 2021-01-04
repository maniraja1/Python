from random import randint
def pivotdata(array: list, left: int, right: int, pivot: int)->(list, int):
    pivot_value = array[pivot]
    new_pivot = left
    print(f"Inner function: {pivot_value, left, pivot, right, array }")
    array[right], array[pivot]=array[pivot], array[right]

    for i in range(left, right):
        if array[i]>pivot_value:
            array[i], array[new_pivot]=array[new_pivot], array[i]
            new_pivot += 1
    array[right], array[new_pivot] = array[new_pivot], array[right]
    return array, new_pivot

def kthlargest(array: list, k: int)->int:
    left, right = 0, len(array)-1
    while left <= right:
        pivot = randint(left, right)
        array, pivot = pivotdata(array, left, right, pivot)
        print(array, left, pivot, right)
        if pivot == k-1:
            return array[pivot]
        elif pivot > k-1:
            right = pivot-1
        else:
            left = pivot+1

x=[1,2,3,4,5,6,7,8,9]
x=[1,1,1,1,1,1,8,9,10]
print(kthlargest(x, 5))
