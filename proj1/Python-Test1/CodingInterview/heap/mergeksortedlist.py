import heapq

def mergeksortedlist(arrays: list)->list:
    min=[]
    result = []
    heapq.heapify(min)
    sorted_arrays_iter = [iter(x) for x in arrays]

    for i,x in enumerate(sorted_arrays_iter):
        heapq.heappush(min, (next(x),i))

    print(min)

    while len(min) >0:
        val,ctr = heapq.heappop(min)
        result.append(val)
        try:
            heapq.heappush(min, (next(sorted_arrays_iter[ctr]), ctr))
        except StopIteration:
            continue
    print(result)


mergeksortedlist([[1,2,7],[4,5,9], [3,6,8]])

import heapq
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        min = []
        result = []
        heapq.heapify(min)
        for x in lists:
            head = x
            while head is not None:
                heapq.heappush(min, head.val)
                head = head.next

        print(min)
        dummy = ListNode(-1)
        head = dummy
        while len(min) > 0:
            val = heapq.heappop(min)
            node = ListNode(val)
            head.next = node
            head = head.next
        return dummy.next


x=[ListNode(val= 1, next= ListNode(val= 4, next= ListNode(val= 5, next= None))),
 ListNode(val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= None))),
 ListNode(val= 2, next= ListNode(val= 6, next= None))]


x=Solution().mergeKLists(x)
head=x
while head is not None:
    print(head.val)
    head=head.next






