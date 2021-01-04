# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.i = 0
        self.val=None
    def kthnode(self, root: TreeNode, k: int) -> int:
        if self.val is not None:
            return self.val

        if root is not None:
            self.kthnode(root.left, k)
            if self.i == k and self.val is  None:
                self.val =  root.val
            self.i += 1
            self.kthnode(root.right, k)
        return self.val


root = TreeNode(1)
root.left      = TreeNode(2)
root.right     = TreeNode(3)
root.left.left  = TreeNode(4)
root.left.right  = TreeNode(5)

print(Solution().kthnode(root, 5))


