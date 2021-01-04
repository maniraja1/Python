# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, postorder, inorder):
        imap = dict()
        for i,j in enumerate(inorder):
            imap[j]=i
        return self.helper(postorder, 0,len(postorder)-1,inorder,0, len(inorder)-1, imap, 'root')

    def helper(self, postorder, pleft, pright, inorder, ileft, iright, imap, direction):
        #print('v', pleft, pright, ileft, iright, direction)
        if pleft > pright or ileft > iright:
            return None
        i=imap[postorder[pright]]
        #print(postorder[pright], pleft, pright, ileft, iright, i)
        root = TreeNode(postorder[pright])

        root.right = self.helper(postorder, pleft-ileft+i, pright-1, inorder, i+1, iright, imap, 'right')
        root.left = self.helper(postorder, pleft, pleft-ileft+i-1, inorder,  ileft, i-1, imap, 'left')

        return root

def preorder_traversal(root: TreeNode):

    if root is not None:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


postorder = [9,15,7,20,3]
inorder = [9,3,15,20,7]

x=Solution().buildTree(postorder, inorder)
print(type(x))
preorder_traversal(x)