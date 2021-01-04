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


def del_dupe(x:linked_list):
    start,second = x.head, x.head.next

    while start is not None and second is not None:
        if start.data==second.data:
            start.next=second.next
            second = second.next
        else:
            start=start.next
            second=second.next

print('#'*75)
print("Original List")
x1=linked_list(1)
x1.append_items([2, 2, 2, 3, 4, 5])
print(f"x1: {list(x1.traverse())}")
del_dupe(x1)
print(f"x1: {list(x1.traverse())}")