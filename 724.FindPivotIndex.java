import java.util.Arrays;

class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0;
        int tmp = 0;
        for (int num: nums) {
            sum += num;
        }
        for (int i = 0; i < nums.length; i += 1) {
            if (i != 0) {
                tmp += nums[i - 1];
            }
            if (sum - tmp - nums[i] == tmp) {
                return i;
            }
        }
        return -1;
    }
}