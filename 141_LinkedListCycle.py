# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        Given a linked list, determine if it has a cycle in it.
        :type head: ListNode
        :rtype: bool
        """
        hare, tortoise = head, head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                return True
        
        return False