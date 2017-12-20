import java.util.Arrays;

class Solution {
    public int missingNumber(int[] nums) {
        int result = 0;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length + 1; i += 1) {
            if (i == nums.length) {
                return nums.length;
            }
            if (i != nums[i]) {
                result = i;
                break;
            }
        }
        return result;
    }
}