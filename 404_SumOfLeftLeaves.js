/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumOfLeftLeaves = function(root) {
    tra(root, false);
    return c;
};

var c = 0;

function tra(node, should) {
    if (!node) {
        return;
    }
    if (!node.left && !node.right) {
        if (should) {
            c += node.val;
        }
        return;
    } else {
        tra(node.left, true);
        tra(node.right, false);
    }
}