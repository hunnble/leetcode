class Solution {
    public int findLengthOfLCIS(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int tmp = 1;
        int result = 1;
        for (int i = 1; i < nums.length; i += 1) {
            if (nums[i] > nums[i - 1]) {
                tmp += 1;
            } else {
                result = result < tmp ? tmp : result;
                tmp = 1;
            }
        }
        result = result < tmp ? tmp : result;
        return result;
    }
}
