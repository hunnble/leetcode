/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode result = new ListNode(-1);
        result.next = head;
        ListNode p = result;
        ListNode q = head;
        while (q != null) {
            if (q.val == val) {
                p.next = q.next;
            } else {
                p = p.next;
            }
            q = q.next;
        }
        return result.next;
    }
}
