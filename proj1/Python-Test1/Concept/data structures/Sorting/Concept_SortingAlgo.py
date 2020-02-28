'''
There are two types of sorting algorithm comparison based and non comparison based
comparison: Quick, bubble, merge, insertion, selection
    CComplexity: O(N^2), O(NlogN), O(N)
non comparison: raidx, bucket
    Complexity: O(N)
For comparison based sorting algorithm we have to make logN! comparison which can be brought down to NLogN
so the fastest a comparison sort can do is NLogN.
Adaptive algorithm changes behavior based on input. It takes advantage of subsets that are already sorted
heap sort and merge sort are not adaptive algorithm

Bubble sort
    In place sorting algorithm, stable sorting algorithm
    Complexity: O(N^2)
    compares adjacent pairs till the entire list is sorted
    Not an ideal sorting algorithm

Selection Sort
    Complexity: O(N^2)
    loop through the array and compare the first element with smallest element in the array and swap the elements
    after every iteration your left side of the array is sorted while the right side of the array is unsorted.
    You keep moving this boundary one item at a time  till you reach all the way to the right
    Selection & Insertion sort are faster for smaller sub arrays ~ 10-20 items
    makes lesser writes than insertion sort
    In place algorithm no need for extra memory
    not a stable sort
    Faster than bubble sort

Insertion Sort
    Complexity: O(N^2)
    You start from the second element from left and compare it to the left most item and swap if necessary
    Now consider the third element and compare it with 1 and 2 and swap  if necessary
    Now consider the fourth element and compare it with 1,2 &3 and swap if necessary
    continue till you have reached the end of array
    Faster than bubble & selection sort
    Inefficient on large arrays, faster on smaller arrays ~ 10-20 items
    Adaptive algorithm
    Stable sort
    Online algorithm, it can sort an array as more items are added to it
    Hybrid algorithm uses Insertion sort if the array length is < 20
    If writes are expensive use selection sort if not use insertion sort

Quick Sort
    complexity
        average: O(NLogN)
        worst: O(N^2)
    For implementation watch video
    In place sort
    Not a stable sort
    Well implemented quick sort can outperform heap and merge sort
    widely used in programming languages. primitive types uses quick sort and reference types uses merge sort.
    Above statement is true for java not python

Merge sort
    Time Complexity: O(N LogN)
    Space complexity: O(N)
    Divide the array recursively such that each sub array has only single item. We consider this sub array as sorted
    now start merging the sub array by comparing the items and continue to merge till we have the array sorted.
    see video for more details
    Not an inplace algorithm
    Efficient quick sort outperforms merge sort but quick sort can have O(N^2) time complexity but
    merge sort will always have O(N logN) complexity.
    Merge sort is generally suited for linked list sorting because then it only needs O(1) space complexity
    stable sort
Heapsort
    Here is the pseudocode for heapsort
    https://www.programiz.com/dsa/heap-sort

Hybrid algorithm
    Algorithm that choose sorting algorithm depending on the data or switching algorithm over the course of sorting
    Introsort
        Quicksort+HeapSort
            Starts with Quick sort and when that becomes slower then switches to heap sort
    Timsort
        InsertionSort+MergeSort
            Insertion sort is efficient for small data sets
            Merge sort is more efficient with large data sets
Counting sort
    Complexity:
        Time O(N+K)
        Space O(k)
        N is the number of elements in an array
        k is the diff between max and min item
    This is a non comparison based array
    This is not an inplace sort and also not a stable sort
    ideal if the array has integer values
    It creates an empty array with k slots and then iterates through original array and for each occurence of a value
    it would increment the counter in the new array by 1
    Finally it would iterate through the new array and sort the elements based on the count

Radix sort
    Complexity
        Time: O(n*k)
        Space: ?
        N is the number of elements
        K is he number of digits
        It is a stable sorting algorithm
    LSD
        sorting from right to left
    MSD
        sorting from left to right
        sensitive to ASCII & unicode representation






'''