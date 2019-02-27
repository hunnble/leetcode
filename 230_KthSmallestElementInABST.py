# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        curCount = self.count(root.left)
        if curCount + 1 > k:
            return self.kthSmallest(root.left, k)
        elif curCount + 1 < k:
            return self.kthSmallest(root.right, k - curCount - 1)

        return root.val

    def count(self, node):
        if not node:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)
