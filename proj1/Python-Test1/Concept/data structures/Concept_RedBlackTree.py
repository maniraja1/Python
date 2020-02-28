'''
Data structure that is a tree and acts similar to binary search tree but follows a set of rules to prevent
a tree from being too unbalanced. This is not as strict as AVL tree but also not very lenient as BST.
In a binary search tree there is a possibility that the tree could be unbalanced and the complexity for search/Insert/
Delete could end up being o(n). With RBT complexity always remains as O(LogN)
Rules for RBT
    Each node is either red or black
    The root node is always black
    All leaves are marked as MIL and set to black
    Every red node must have 2 black child and a black parent
    Every path from a give node to any of its descendant (NIL node) has the same number of black nodes
    Every new node is red by default and inserted like we do with BST and set to red
    Post insert We have to check if the tree violates the rules and if yes either rotate or change the node color


'''