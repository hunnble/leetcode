# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
        Note: Do not modify the linked list.
        :type head: ListNode
        :rtype: ListNode
        """
        p, q, circle = head, head, False
        while p and p.next:
            p = p.next.next
            q = q.next
            if p == q:
                circle = True
                break

        if not circle:
            return None
        else:
            counter = 1
            while p.next and p.next != q:
                p = p.next
                counter += 1
            p = head
            while True:
                q = p
                for i in range(0, counter):
                    q = q.next
                if p == q:
                    return p
                p = p.next
