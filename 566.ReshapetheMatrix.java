class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        int r1 = nums.length;
        int c1 = nums[0].length;
        int numsCount = r1 * c1;
        if (numsCount != r * c) {
            return nums;
        }
        int[][] result = new int[r][c];
        for (int i = 0; i < numsCount; i += 1) {
            result[i / c][i % c] = nums[i / c1][i % c1];
        }
        return result;
    }
}