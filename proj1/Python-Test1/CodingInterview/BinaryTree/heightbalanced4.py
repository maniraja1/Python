class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> (bool,int):
        if root is None:
            return True,0

        l = self.isBalanced(root.left)
        r = self.isBalanced(root.right)

        print(l, r, root.val)

        if l[0] is False or r[0] is False:
            return False,max(l[1], r[1])+1


        if abs(l[1]-r[1])>1:
            return False,max(l[1], r[1])+1

        return True, max(l[1], r[1])+1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right= TreeNode(4)

'''root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.left.left.left = TreeNode(7)
#root.left.left.left.left = TreeNode(9)'''

x=Solution().isBalanced(root)
print(x)