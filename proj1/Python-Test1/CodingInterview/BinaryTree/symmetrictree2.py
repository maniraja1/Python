class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def Issymmetric(self, root: TreeNode)->bool:
        if root is None:
            return True
        return self.Issymmetric_subtree(root.left, root.right)

    def Issymmetric_subtree(self, left, right):

        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        x = self.Issymmetric_subtree(left.left,right.right)
        y = self.Issymmetric_subtree(left.right, right.left)
        print(x,y, left.val, right.val, x & y & (left.val == right.val))
        return   x & y & (left.val == right.val)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(3)
root.right.right.right = TreeNode(3)
print(Solution().Issymmetric(root))