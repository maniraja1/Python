# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int, runningdiff=None)->bool:
        if runningdiff is None:
            runningdiff = sum
        if root is None:
            return False

        if root.left is None and root.right is None:
            return runningdiff == root.val

        return self.hasPathSum(root.left, sum, runningdiff-root.val) or \
            self.hasPathSum(root.right, sum, runningdiff - root.val)

root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(2)

print(Solution().hasPathSum(root, 22))
