#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        imap = dict()
        for i, data in enumerate(inorder):
            imap[data] = i
        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, imap, 'root')

    def helper(self, preorder: list, pstart: int, pend: int, inorder: list, istart: int, iend: int,
               imap: dict, direction) -> TreeNode:
        #print('v',pstart,pend,istart,iend, direction )
        if pstart > pend or istart > iend:
            return None
        i = imap[preorder[pstart]]
        #print(preorder[pstart],pstart, pend, istart, iend,i)
        root = TreeNode(preorder[pstart])
        # Build Left subtree
        root.left = self.helper(preorder, pstart + 1, pstart + i - istart, inorder, istart, i - 1, imap, 'left')
        root.right = self.helper(preorder, pstart + i - istart + 1, pend, inorder, i + 1, iend, imap, 'right')

        return root

def preorder_traversal(root: TreeNode):

    if root is not None:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

x=Solution().buildTree(preorder, inorder)
preorder_traversal(x)
