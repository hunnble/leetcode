# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        Reverse a singly linked list.
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
            
        c, r, head.next = head, head.next, None
        while r is not None:
            n = r.next
            r.next = c
            c, r = r, n
        
        return c