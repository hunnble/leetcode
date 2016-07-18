# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def f(node):
            if (node is None):
                return
            tmp = node.left
            node.left = node.right
            node.right = tmp
            f(node.left)
            f(node.right)
        f(root)

        return root