class Node:

    def __init__(self, val=None):
        self.val = val
        self.next=None
        self.prev=None

class Linkedlist:

    def __init__(self, node=None):
        if node is not None:
            node= Node(node)
        self.head=node

    def traverse(self,prnt=False):
        node = self.head
        while node.val is not None:
            if prnt:
                print(f"Value: {node.val}")
            if node.next is None:
                return node
            node = node.next
        return

    def insertend(self, val):
        lastnode =self.traverse()
        node=Node(val)
        lastnode.next = node

    def insertbegin(self, val):
        firstnode = self.head
        node = Node(val)
        node.next=firstnode
        self.head = node

class doublelinkedlist(Linkedlist):

    def __init__(self, val):
        node = Node(val)
        self.head=node

    def insertend(self, val):
        lastnode=self.traverse()
        node=Node(val)
        lastnode.next=node
        node.prev=lastnode

    def insertbegin(self, val):
        node = Node(val)
        self.head.prev=node
        node.next=self.head
        self.head=node


l1 = Linkedlist(1)
print(l1.head.val)
l1.insertend(2)
l1.traverse(True)
l1.insertbegin(3)
l1.traverse(True)
print('#'*50)
l2 = doublelinkedlist(1)
l2.insertbegin(3)
l2.insertend(2)
l2.traverse(True)