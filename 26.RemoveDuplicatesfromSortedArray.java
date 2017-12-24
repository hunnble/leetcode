class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length < 2) {
            return nums.length;
        }
        int result = 1;
        for (int i = 1; i < nums.length; i += 1) {
            if (nums[i - 1] != nums[i]) {
                nums[result] = nums[i];
                result += 1;
            }
        }
        return result;
    }
}