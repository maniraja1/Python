'''
Quick Concept
    A heap is a tree-like data structure where the child nodes have a sort-order relationship with the parents.
    Tree is filled from left to right and there are no missing node is a row
    Binary heaps can be represented using a list or array organized so that the children of element N are at positions
    2*N+1 and 2*N+2 (for zero-based indexes). This is because rows needs to be filled left to right before moving on.
    This layout makes it possible to rearrange heaps in place, so it is not necessary to reallocate as much memory when
    adding or removing items.
    A max-heap ensures that the parent is larger than or equal to both of its children. A min-heap requires that the
    parent be less than or equal to its children. Python’s heapq module implements a min-heap.

Module
    from heapq import nsmallest,heapify,heappop,heappush
Methods
    heapq.heappush  # Push an element to heap
    heapq.heappop   # Pop and return the smallest item from the heap, maintaining the heap invariant.
    heapq.heapify   # Transform list x into a heap, in-place, in linear time.
    heapq.pushpop   # Push item on the heap, then pop and return the smallest item from the heap
    heapq.heapreplace # Pop and return the smallest item from the heap, and also push the new item.
    heapq.merge
    heapq.nlargest # Return a list with the n largest elements from the dataset
    heapq.nsmallest # Return a list with the n smallest elements from the dataset
Notes
    heapify transforms a list to heap in place
    If the heap is empty, IndexError is raised when you run heappop.
    To access the smallest item without popping it, use heap[0].
    A max-heap ensures that the parent is larger than or equal to both of its children.
    A min-heap requires that the parent be less than or equal to its children.
    aq  `Python's heapq module implements a min-heap.
    Example 1.0 Create a heap from list
    Example 2.0 heappush
    Example 3.0 nsmallest

Complexity for heap
    Memory complexity = O(N)
    Insert = O(1)(insert)+O(LogN)(heap validation) ~ O(LogN) ~ O(Log2(N)
            because any node will only have Log2N parents so only Log2N swaps are required
    remove = O(1)(delete) + O(LogN) (heap validation)

                    Binary      Binomial        Fibonacci
    FindMin         O(1)        O(1)            O(1)
    DeleteMin       O(log n)    O(log n)        O(log n)
    Insert          O(log n)    O(1)            O(1)
    DecreaseKey     O(log n)    O(log n)        O(1)
    Merge                       O(log n)        O(1)

Other Heap types
    Binomial heap
        similar to binary heap but supports quick merging of two heaps
        implementation of mergeable heap abstract data type
        priority queue supporting merge operationsƒ
        binomial heap is implemented as a collection of tree
        insertion O(log n) can be changed to O(1) with binomial heaps
    Fibonacci heap
        faster than binary heaps
        very hard to implement
        can have several children, however number of children are kept low
        can achieve insert time complexity of O(1)



'''
from heapq import nsmallest,heapify,heappop,heappush
# Example 1.0
print('Example 1.0')
x = [10,2,7,3,9,4,8,5]
heapify(x)
print(heappop(x))

# Example 2.0
print('Example 2.0')
x = [10,2,7,3,9,4,8,5]
heapify(x)
print(heappop(x))
heappush(x,1)
print(heappop(x))

