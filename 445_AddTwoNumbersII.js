/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    l1 = reverseList(l1);
    l2 = reverseList(l2);
    var r = [];
    var t = 0;
    while(l1 || l2) {
        if (l1 && l2) {
            l1.val += l2.val + t;
            t = parseInt(l1.val / 10, 10);
            l1.val %= 10;
            l2 = l2.next;
        } else if (l1) {
            l1.val += t;
            t = parseInt(l1.val / 10, 10);
            l1.val %= 10;
        } else {
            l1 = {
                val: l2.val
            };
            l1.val += t;
            t = parseInt(l1.val / 10, 10);
            l1.val %= 10;
            l2 = l2.next;
        }
        r.unshift(l1.val);
        l1 = l1.next;
    }
    if (t) {
        r.unshift(t);
    }
    return reverseList(r);
};

function reverseList(head) {
    var p = null, q = head, r = null;
    while(q) {
        r = q.next;
        q.next = p;
        p = q;
        q = r;
    }
    return p;
}
