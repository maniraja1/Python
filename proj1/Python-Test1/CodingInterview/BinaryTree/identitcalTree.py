# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Identical(t1, t2)->bool:

    if t1 is None and t2 is None:
        return True
    if t1 is not None and t2 is not None:
        return t1.val == t2.val and Identical(t1.left, t2.left) and Identical(t1.right, t2.right)
    else:
        return False


x = TreeNode(15)
x.left = TreeNode(10)
x.right = TreeNode(20)
x.left.left = TreeNode(8)
x.left.right = TreeNode(12)
x.right.left = TreeNode(16)
x.right.right = TreeNode(25)

# construct second tree
y = TreeNode(15)
y.left = TreeNode(10)
y.right = TreeNode(20)
y.left.left = TreeNode(8)
y.left.right = TreeNode(12)
y.right.left = TreeNode(16)
y.right.right = TreeNode(25)
y.right.right.right = TreeNode(25)
print(Identical(x, y))
