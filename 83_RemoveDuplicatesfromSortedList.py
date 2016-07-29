# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        Given a sorted linked list, delete all duplicates such that each element appear only once.
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
            
        p, q = head, head
        while p:
            while q and p.val == q.val:
                q = q.next
            p.next, p = q, q
        
        return head