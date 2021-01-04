# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return None
        return self.sumNumbers2(root, 0)

    def sumNumbers2(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return sum * 10 + root.val

        return self.sumNumbers2(root.left, sum * 10 + root.val) \
               + self.sumNumbers2(root.right, sum * 10 + root.val)






root = TreeNode(1)
root.left = TreeNode(0)

print(Solution().sumNumbers(root))

