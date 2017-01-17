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
    return tra(root, false);
};

function tra(node, should) {
    if (!node) {
        return 0;
    }
    if (!node.left && !node.right) {
        return should ? node.val : 0;
    }
    return tra(node.left, true) + tra(node.right, false);
}