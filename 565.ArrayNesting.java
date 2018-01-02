class Solution {
    public int arrayNesting(int[] nums) {
        int result = 0;
        for (int i = 0; i < nums.length; i += 1) {
            int size = 0;
            for (int j = i; nums[j] >= 0; size += 1) {
                int tmp = nums[j];
                nums[j] = -1;
                j = tmp;
            }
            result = Math.max(result, size);
        }
        return result;
    }
}