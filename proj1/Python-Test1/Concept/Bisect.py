'''
Extremely useful for searching in a sorting array.

Bisect: This function returns the position in the sorted list, where the number passed in argument can
be placed so as to maintain the resultant list in sorted order. If the element is already present in
the list, the right most position where element has to be inserted is returned

bisect_left: This function returns the position in the sorted list, where the number passed in argument
can be placed so as to maintain the resultant list in sorted order. If the element is already present
in the list, the left most position where element has to be inserted is returned.

bisect_right: Functions similarly to bisect

'''


# bisect
import bisect
l = [1,2,2,2,2,3,4,5]
print(bisect.bisect(l,2)) #
print(bisect.bisect_right(l,2))
print(bisect.bisect_left(l,2))