class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int result = 0;
        int temp = 0;
        for (int i = 0; i < nums.length; i += 1) {
            if (nums[i] == 1) {
                temp += 1;
            } else {
                if (temp > result) {
                    result = temp;
                }
                temp = 0;
            }
        }
        if (temp > result) {
            result = temp;
        }
        return result;
    }
}