class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leftview(root: TreeNode,direction='root'):
    if root is None:
        return

    if direction in ('root', 'left'):
        print (root.val, direction)

    if direction == 'right' and root.left is None and root.right is None:
        print(root.val, direction)

    leftview(root.left, 'left')
    leftview(root.right, 'right')


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)

leftview(root, 'root')