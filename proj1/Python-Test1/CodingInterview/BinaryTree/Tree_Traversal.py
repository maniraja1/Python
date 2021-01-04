class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root: TreeNode):

    if root is not None:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root: TreeNode):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def inorder(root: TreeNode):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)




root = TreeNode(1)
root.left      = TreeNode(2)
root.right     = TreeNode(3)
root.left.left  = TreeNode(4)
root.left.right  = TreeNode(5)
#print(preorder(root))
#postorder(root)
inorder(root)
