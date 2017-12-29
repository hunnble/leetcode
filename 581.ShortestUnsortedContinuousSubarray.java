class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int l = nums.length;
        int beg = -1;
        int end = -2;
        int max = nums[0];
        int min = nums[l - 1];
        for (int i = 1; i < l; i += 1) {
            max = Math.max(max, nums[i]);
            min = Math.min(min, nums[l - 1 - i]);
            if (nums[i] < max) {
                end = i;
            }
            if (nums[l - 1 - i] > min) {
                beg = l - 1 - i;
            }
        }
        return end - beg + 1;
    }
}