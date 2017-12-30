class Solution {
    public void rotate(int[] nums, int k) {
        int l = nums.length;
        k %= l;
        reverse(nums, 0, l - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, l - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        int tmp = 0;
        while (start < end) {
            tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start += 1;
            end -= 1;
        }
    }
}