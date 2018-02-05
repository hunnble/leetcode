/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        if(root == null) {
            return 0;
        }
       int dis = depth(root.left) + depth(root.right);
       int ldis = diameterOfBinaryTree(root.left);
       int rdis = diameterOfBinaryTree(root.right);
       return Math.max(dis, Math.max(ldis, rdis));
    }

    public int depth(TreeNode root){
        if(root == null) {
            return 0;
        }
        return 1 + Math.max(depth(root.left), depth(root.right));
    }
}
