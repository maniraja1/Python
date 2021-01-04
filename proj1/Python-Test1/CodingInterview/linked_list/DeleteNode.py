'''
Delete Kth element from a list.
We can traverse the list till we reach the index.
As we traverse keep track of the previous node.
Link prev.next to curr.next.next
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

    def updatenext(self, node, next):
        node.next = next

    def len(self):
        start = self.head
        l = 1
        while start.next is not None:
            l += 1
            start = start.next
        return l

    def delete(self,indx):

        if indx==1:
            self.head = self.head.next
        elif 1 < indx <= self.len():
            i=1
            pos = self.head
            while i < indx:
                prev=pos
                pos = pos.next
                i += 1
            prev.next=pos.next
        else:
            raise ValueError("Incorrect Index passed")

print('#'*75)
print("Original List")
x1=linked_list(1)
x1.append_items([2, 3, 4, 5])
print(f"x1: {list(x1.traverse())}")
print('#'*75)
print("Delete Index 3")
x1.delete(3)
print(f"x1: {list(x1.traverse())}")
print('#'*75)
print("Delete Index 1")
x1=linked_list(1)
x1.append_items([2, 3, 4, 5])
x1.delete(1)
print(f"x1: {list(x1.traverse())}")
print('#'*75)
print("Delete Index 5")
x1=linked_list(1)
x1.append_items([2, 3, 4, 5])
x1.delete(5)
print(f"x1: {list(x1.traverse())}")
print('#'*75)
print("Delete Index 9")
x1=linked_list(1)
x1.append_items([2, 3, 4, 5])
x1.delete(9)
print(f"x1: {list(x1.traverse())}")
