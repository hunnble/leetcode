# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        Given a linked list, swap every two adjacent nodes and return its head.
        For example,
        Given 1->2->3->4, you should return the list as 2->1->4->3.
        Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
        :type head: ListNode
        :rtype: ListNode
        """
        rh = ListNode(0)
        rh.next = head
        p = rh
        while p.next and p.next.next:
            t = p.next
            p.next = p.next.next
            t.next = p.next.next
            p.next.next = t
            p = t
        
        return rh.next