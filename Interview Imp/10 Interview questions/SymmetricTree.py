class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def tree_sum(self, root):
        if root is None:
            return 0
        left = self.tree_sum(root.left)
        right = self.tree_sum(root.right)
        return root.val+left+right


def symmetericTree(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None != root2 is None or root1.val != root2.val:
        return False

    return symmetericTree(root1.left, root2.right) and symmetericTree(root1.right, root2.left)
