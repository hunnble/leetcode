class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int result = 0;
        int tmp = 0;
        for (int i = 0; i < k; i += 1) {
            result += nums[i];
        }
        tmp = result;
        for (int i = 0; i < nums.length - k; i += 1) {
            tmp -= nums[i];
            tmp += nums[i + k];
            result = Math.max(tmp, result);
        }
        return result / 1.0 / k;
    }
}