class Solution {
    public int[] productExceptSelf(int[] nums) {
        int l = nums.length;
        int[] result = new int[l];
        int tmp = 1;
        for (int i = 0; i < l; i += 1) {
            result[i] = tmp;
            tmp *= nums[i];
        }
        tmp = 1;
        for (int i = l - 1; i >= 0; i -= 1) {
            result[i] *= tmp;
            tmp *= nums[i];
        }
        return result;
    }
}