'''
Data structure that links nodes together. The actual data is stored inside the node.
Each node represents data (like an array element) and each node also holds a reference to its previous and next item.

Single linked list only has reference to the next item
double linked list has reference to next and previous item

Complexity
    insert = O(1)
    delete = O(1)
    search = O(n)
    GetFirstElement=O(1)
    GetNextElement = O(1)
    Get PreviousElement=O(1)

    As you can see its efficient in inserting and deleting items.
    It is very inefficient when searching items in a linked list
    However it is great at looking for next and previous element.
    This is a great data structure for undo & redo or back and forward button in a browser

'''



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