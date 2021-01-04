class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class linked_list:

    def __init__(self, val=None):
        node = Node(val)
        self.head = node
        self.tail = node

    def traverse(self):
        cur = self.head
        while cur is not None:
            x = cur.val
            cur = cur.next
            yield x

    def append(self, val):
        node = Node(val)
        if self.head.val is None:
            self.head=node
        self.tail.next = node
        self.tail = node

    def pop(self):
        self.head = self.head.next


print('#'*75)
print("Demo linked list")
x = linked_list(1)
x.append(2)
x.append(3)
print(list(x.traverse()))
x.pop()
print(list(x.traverse()))
print(x.tail.val)
print('#'*75)
print("Merge two sorted list")
l1 = linked_list(1)
l1.append(3)
l1.append(5)

l2 = linked_list(2)
l2.append(4)
l2.append(6)
l2.append(8)
l2.append(10)

print(f"Original list L1: {list(l1.traverse())}")
print(f"Original List L2: {list(l2.traverse())}")



sorted_list=linked_list()

while l1.head is not None and l2.head is not None:
    if l1.head.val < l2.head.val:
        sorted_list.append(l1.head.val)
        l1.head = l1.head.next

    else:
        sorted_list.append(l2.head.val)
        l2.head = l2.head.next


for y in l1.traverse():
    sorted_list.append(y)

for y in l2.traverse():
    sorted_list.append(y)

print(list(sorted_list.traverse()))



