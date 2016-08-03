# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        root.dis = 0
        queue, r = [root], []
        while len(queue) > 0:
            node = queue.pop(0)
            if len(r) <= node.dis:
                r.insert(0, [])
            r[0].append(node.val)
            if node.left:
                node.left.dis = node.dis + 1
                queue.append(node.left)
            if node.right:
                node.right.dis = node.dis + 1
                queue.append(node.right)

        return r
