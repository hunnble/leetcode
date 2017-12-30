class Solution {
    public boolean checkPossibility(int[] nums) {
        int times = 0;
        for (int i = 1; i < nums.length; i += 1) {
            if (nums[i - 1] > nums[i]) {
                times += 1;
                if (i == 1 || nums[i - 2] <= nums[i]) {
                    nums[i - 1] = nums[i];
                } else {
                    nums[i] = nums[i - 1];
                }
            }
        }
        return times <= 1;
    }
}