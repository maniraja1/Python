'''
Pivoting involves sorting the list such that
1.all items <k appears to the left
2.items equal to k appears next
3.and items > k appears to the right

create 3 empty nodes and start arranging the list depending on if value is <,= or > k by
looping through the linked list
once you are done you need to arrange
1.high.next=None
2.equal.next=high.head
3.low.next=equal.head


'''


class list_node:
    def __init__(self, val=0, next=None):
        self.data=val
        self.next = next

    def traverse(self):
        cur = self
        while cur is not None:
            xout = cur.data
            cur = cur.next
            yield xout


class linked_list:

    def __init__(self, val=None):
        node = list_node(val)
        self.head = node
        self.tail = node

    def append(self, val):
        node = list_node(val)
        self.tail.next = node
        self.tail = node

    def append_items(self, vals):
        for x in vals:
            self.append(x)

    def traverse(self):
        return self.head.traverse()

    def len(self):
        i=1
        start = self.head
        while start.next is not None:
            start = start.next
            i += 1
        return i

def pivot(l:linked_list, k:int):
    low = low_head=list_node(None)
    equal = equal_head = list_node(None)
    high = high_head=list_node(None)
    start=l.head
    while start.data is not None:
        if start.data < k:
            low.next=start
            low=start
            print(f"Added {start.data} to low")
        elif start.data == k:
            equal.next=start
            equal=start
        else:
            high.next=start
            high=start
        start = start.next
        if start.next is None:
            break

    high.next = None
    equal.next = high_head.next
    low.next = equal_head.next
    low_head=low_head.next
    return low_head

print('#'*75)
print("Original List")
x1=linked_list(1)
x1.append_items([2,3, 4, 2, 3, 7, 8, 6, 1])
print(f"x1: {list(x1.traverse())}")
x2=pivot(x1, 4)
print(f"x1: {list(x2.traverse())}")


