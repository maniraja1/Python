'''
Data structure that is a tree and acts similar to binary search tree but is balanced.
This is also called as AVL tree.
In a binary search tree there is a possibility that the tree could be unbalanced and the complexity for search/Insert/
Delete could end up being o(n)
In a balanced binary tree it ensures that the tree is always balanced and so complexity will always be o(logN)
The difference in the heights of child sub tree for any node should not be greater than 1
Node.height = max(leftchild.height, rightchild.height)+1
When a node is unbalanced you need to rotate the node left or right.
If the tree is right heavy rotate left
If the tree is left heavy rotate right

'''