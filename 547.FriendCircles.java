class Solution {
    public int findCircleNum(int[][] M) {
        int len = M.length;
        int result = 0;
        int[] root = new int[len];
        for (int i = 0; i < len; i += 1) {
            root[i] = i;
        }
        for (int i = 0; i < len; i += 1) {
            for (int j = i + 1; j < len; j += 1) {
                if (M[i][j] == 1) {
                    unionFind(root, i, j);
                }
            }
        }
        for (int i = 0; i < len; i += 1) {
            if (root[i] == i) {
                result += 1;
            }
        }
        return result;
    }

    private void unionFind(int[] root, int i, int j) {
        while (root[i] != i) {
            i = root[i];
        }
        while (root[j] != j) {
            j = root[j];
        }
        if (root[i] != root[j]) {
            root[j] = i;
        }
    }
}
