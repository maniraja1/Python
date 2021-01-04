class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class linked_list:

    def __init__(self, node=None):
        node = Node(node)
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
        self.tail.next = node
        self.tail = node

    def pop(self):
        self.head = self.head.next
