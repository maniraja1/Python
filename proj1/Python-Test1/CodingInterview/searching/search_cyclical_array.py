'''
From a cyclically sorted array find the smallest element.
Cyclically sorted array is one which if you shift elements left or right then the array
gets sorted

Example 8, 9, 10, 1, 2, 3, 4, 5, 6, 7
In the above example if we shift array left 3 times the array is sorted

The key to understanding this algorithm is
if A[mid]> A[right] then the smallest value is somewhere between A[mid+1:right+1]
if A[mid]<A[right] then the smallest value is between A[left:mid]. The current element can also
be the smallest element that is wht its not A[left:mid-1]

'''
def findsmallest(array: list)-> int:
    left, right = 0, len(array)-1

    while left < right:
        print(left, right)
        mid = (left+right)//2

        if array[mid]>array[right]:
            left = mid+1
        else:
            right= mid
    print(left)

x=[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
findsmallest(x)