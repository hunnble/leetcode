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
    public TreeNode convertBST(TreeNode root) {
        dfs(root, 0);
        return root;
    }

    private int dfs(TreeNode root, int val) {
        if (root == null) {
            return val;
        }
        int right = dfs(root.right, val);
        int left = dfs(root.left, root.val + right);
        root.val = root.val + right;
        return left;
    }
}
