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
var maxDepth = function(root) {
    var depth = 0,
    	nodes = [root],
    	node;
    
    if (!root) {
		return depth;
	}
    root.val = 1;
    while(nodes.length > 0) {
    	node = nodes.pop();
    	if (node.val > depth) {
    		depth = node.val;
    	}
    	if(node.left) {
    		node.left.val = node.val + 1;
    		nodes.unshift(node.left);
    	}
    	if(node.right) {
    		node.right.val = node.val + 1;
    		nodes.unshift(node.right);
    	}
    }
    return depth;
};