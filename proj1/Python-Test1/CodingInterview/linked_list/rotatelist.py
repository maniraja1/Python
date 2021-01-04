'''
TO cycle a list k units right
1. Write a function to determine the length of the list
2. start by navigating to len(list)-k
3. len(list)-k = New Tail
4. Hook the old tail to old start
5. start.next is the new head


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

    def rotate(self, k):

        start = self.head
        i=1

        while i< self.len()-k:
            start = start.next
            i += 1
        self.tail.next=self.head
        self.head = start.next
        self.tail=start
        start.next = None




print('#'*75)
print("Original List")
x1=linked_list(1)
x1.append_items([2, 3, 4, 5, 6])
print(f"x1: {list(x1.traverse())}")
x1.rotate(3)
print(f"x1: {list(x1.traverse())}")