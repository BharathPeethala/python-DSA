class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        self.res = []
        self.inOrder(root)
        return self.res

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            self.res.append(root.val)
            self.inOrder(root.right)
