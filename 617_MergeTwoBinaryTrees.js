/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} t1
 * @param {TreeNode} t2
 * @return {TreeNode}
 */
var mergeTrees = function(t1, t2) {
  return merge(t1, t2);
};

var merge = function(n1, n2) {
  if (!n1 && !n2) {
    return null;
  }

  var node = new TreeNode(0);

  node.val = (n1 ? n1.val : 0) + (n2 ? n2.val : 0);
  if ((n1 && (n1.left || n1.right)) || (n2 && (n2.left || n2.right))) {
    node.left = merge(n1 ? n1.left : null, n2 ? n2.left : null);
    node.right = merge(n1 ? n1.right : null, n2 ? n2.right : null);
  }

  return node;
}
