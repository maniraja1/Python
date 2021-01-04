'''
Linked list overlap means one linked list contains the other linked list
x1:1,2,3,40,50,60
x2:40,50,60
x1 overlaps x2

The algorithm works by looking at the diffing the length of the 2 list
and traversing the largest of the 2 linked list by diff units

Now both linked list have the same length to traverse till it reaches the end
At each step you can compare the two lists and if they match then you know that the lists overlap

Same logic can be used for intersection
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

    def append(self,val):
        node = list_node(val)
        self.tail.next=node
        self.tail = node

    def append_items(self, vals):
        for x in vals:
            self.append(x)

    def traverse(self):
        return self.head.traverse()

    def updatenext(self, node, next):
        node.next=next

    def len(self):
        start = self.head
        l = 1
        while start.next is not None:
            l += 1
            start = start.next
        return l

def findintersection(x1:linked_list, x2:linked_list):
    x1_len = x1.len()
    x2_len = x2.len()

    if x1.tail != x2.tail:
        print("Tails do not match. The 2 lists do not seem to intersect")
        return False
    else:
        print("Tails match")

    diff = abs(x1_len-x2_len)
    print(f"Diff: {diff}")
    if x1_len < x2_len:
        x1, x2= x2, x1

    i=1
    x1 = x1.head
    x2 = x2.head

    while i <= diff:
        x1 = x1.next
        i += 1

    while x1 is not None and x2 is not None:
        if x1==x2:
            print(f"Intersecting Node: {x1.data}")
            return True
        x1 = x1.next
        x2 = x2.next
        if x1 is None or x2 is None:
            return False



print('#'*75)
x1=linked_list(1)
x1.append_items([2,3])
print(f"x1: {list(x1.traverse())}")

print('#'*75)
x2=linked_list(10)
x2.append_items([20, 30])
print(f"x2: {list(x2.traverse())}")


x2.append(40)
x1.tail.next = x2.head
x2.append_items([50, 60])
x1.tail=x2.tail
print('#'*75)
print(f"x1: {list(x1.traverse())}")
print(f"x2: {list(x2.traverse())}")
print(f"Tail x1: {x1.tail.data}")
print(f"Tail x2: {x2.tail.data}")

print('#'*75)
print(findintersection(x1, x2))

x3=linked_list(10)
x3.append_items([20,30,40,50,60])
print('#'*75)
print(f"x3: {list(x3.traverse())}")
print(findintersection(x1, x3))