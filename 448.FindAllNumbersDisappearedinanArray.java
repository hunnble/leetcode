import java.util.ArrayList;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> result = new ArrayList<>();
        int len = nums.length;
        for (int i = 0; i < len; i += 1) {
            nums[(nums[i] - 1) % len] += len;
        }
        for (int i = 0; i < len; i += 1) {
            if (nums[i] <= len) {
                result.add(i + 1);
            }
        }
        return result;
    }
}