/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
	if (!root) {
		return [];
	}
    var stack = [];
    var result = [];
    var node = root;
    while(stack.length > 0 || node) {
    	if (node) {
    		stack.unshift(node);
    		node = node.left;
    	} else {
    		node = stack[0];
    		stack.shift();
    		result.push(node.val);
    		node = node.right;
    	}
    }

    return result;
};