#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_of_leaves(root, l=None):
    if root is None:
        return ''

    if root.left is None and root.right is None:
        l.append(root.val)
        return root.val

    return list_of_leaves(root.left, l), list_of_leaves(root.right, l)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(3)
root.right.right.right = TreeNode(3)
l = []
print(list_of_leaves(root,l))
print(l)