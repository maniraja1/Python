'''
Data structure that is a tree where
    the left of the tree is smaller than the parent
    the right of the tree is greater than the parent
If you travel all the way to the left you get the smallest element
If you travel all the way to the right you get the largest element
predecessor = the right most element on the left side of the tree
successor = the first element on the right
Successor and predecessor are important when you delete the parent and you need to know
InorderTraversal = Left sub tree -> root -> right sub tree recursively. Results in sorting all the elements
preorder traversal = root node -> left sub tree -> right sub tree recursively
postorder traversal = left sub tree -> right sub tree -> root node recursively.
binary search tree can be balanced or unbalanced.
When unbalanced this could result in poor performance because it is the same as linked list


Complexity
    Insert = O(log n)+O(1) ~ O(log n)
    Delete = O(log n)+O(1) ~ O(log n)
    search = O(log n)
Note that the time complexity above are average case, the worst case could result in O(n) complexity
'''
import time
class Node:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.val})"

class BTree:
    def __init__(self, val):
        self.root = Node(val)
        self._OpenParent = None

    # Function to get the last node left or right where we can insert the given value
    def getLastNode(self, val, node):
        self._OpenParent = node  # This is the parent that is open and can have a child node.
        time.sleep(1)
        if node.val > val:
            if node.left is not None:
                node = node.left
                self.getLastNode(val, node)  # Recursively call the function
            else:
                return self._OpenParent
        else:
            if node.right is not None:
                node = node.right
                self.getLastNode(val, node)  # Recursively call the function
            else:
                return self._OpenParent

    def insert(self, val):
        node2 = Node(val)
        if val < self.root.val and self.root.left is None:
            self.root.left = node2
        elif val > self.root.val and self.root.right is None:
            self.root.right = node2
        else:
            self.getLastNode(val, self.root)
            time.sleep(1)
            if val < self._OpenParent.val:
                self._OpenParent.left = node2
            else:
                self._OpenParent.right = node2




x = BTree(3)
x.insert(2)
x.insert(5)
x.insert(6)
x.insert(1)
print(x.root.val)
print(x.root.left)
print(x.root.right)
print(x.root.left.val)
print(x.root.right.val)
print(x.root.right.right.val)
print(x.root.left.left.val)
