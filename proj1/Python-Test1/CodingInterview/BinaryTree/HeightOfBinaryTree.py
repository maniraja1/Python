# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def height(root: TreeNode, k: int)-> int:
    if root is None:
        return k-1
    k += 1
    return max(height(root.left, k), height(root.right, k))


x = TreeNode(15)
x.left = TreeNode(10)
x.right = TreeNode(20)
x.left.left = TreeNode(8)
x.left.right = TreeNode(12)
x.right.left = TreeNode(16)
x.right.right = TreeNode(25)
x.right.right.right = TreeNode(25)
print(height(x, 0))