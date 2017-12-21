class Solution {
    public int removeElement(int[] nums, int val) {
        int result = 0;
        for (int i = 0; i < nums.length; i += 1) {
            if (nums[i] != val) {
                nums[result] = nums[i];
                result += 1;
            }
        }
        return result;
    }
}