'''
The algorithm to find cycles is pretty simple
You start from the head and have 2 counters. One counter increments by one
and the other by two. when these two counters meet at the same node then there is a cycle

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


def find_cycle(head):
    fast = slow = head
    while slow.next is not None and fast.next.next is not None:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            print("Cycle Found")
            return slow
    print("No cycle found")
    return None

x=linked_list(1)
x.append_items([2,3,4,5,6,7,8,9,10])
print(list(x.traverse()))
print(f"Cycle head is set at : {find_cycle(x.head)}")
x.updatenext(x.tail, x.head)
#x.tail.next=x.head
print(f"Cycle head is set at : {find_cycle(x.head).data}")
x.updatenext(x.tail.next.next.next, x.head.next.next.next.next)
print(f"Cycle head is set at : {find_cycle(x.head).data}")





