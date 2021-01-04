
'''
Dutch Flag. You pass in input.
Rearrange the array such that
1. elements less than pivot appear first
2. followed by elements equal to pivot f
3. followed elements greater than pivot

Divide the array into 3 portions low, middle, high.
middle starts at 0 and keeps incrementing if it is <= pivot
low increments if there is a swap
high decrements if there is a swap

Here you set
low=0
j=0
high=len(a)-1
You loop while j <= high
    You compare j with pivot
        if < pivot
            swapt low and j
            j++, low++
        if > pivot
            swap high and j
            high++
        if = pivot
            j++
When you swap on the high end notice that you do not increment j
you recheck the index again to see if it is greater than pivot

Time complexity O(n)
space complexity O(1)

'''
def sortColors(A, pivot):
    low, j, high = 0, 0, len(A) - 1
    while j <= high:
        print(A)
        print(low, j, high, pivot)
        if A[j] < pivot:
            A[low], A[j] = A[j], A[low]
            low += 1
            j += 1
        elif A[j] > pivot:
            A[j], A[high] = A[high], A[j]
            high -= 1
        else:
            j += 1
        print(A)
        print(low, j, high, pivot)
        print("#"*50)



A = [0,1,1,2,0,1,0,1]
sortColors(A,1)
print(A)
print("$#"*50)
A = [5,4,4,5,3,3]
sortColors(A,4)
print(A)
A = [6,5,4,8,4,5,2,3,3,7,]
sortColors(A,5)
print(A)
A = [0,1,1,0,0,0,1,1]
sortColors(A,1)
print(A)