import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> m1 = new HashMap<>();
        Map<Integer, Integer[]> m2 = new HashMap<>();
        int degree = 0;
        int result = nums.length;
        for (int i = 0; i < nums.length; i += 1) {
            m1.put(nums[i], m1.getOrDefault(nums[i], 0) + 1);
            degree = Math.max(degree, m1.get(nums[i]));
            if (m2.get(nums[i]) == null) {
                m2.put(nums[i], new Integer[2]);
            }
            Integer[] range = m2.get(nums[i]);
            if (range[0] == null) {
                range[0] = i;
            }
            range[1] = i;
        }
        for (Map.Entry<Integer, Integer> entry: m1.entrySet()) {
            if (entry.getValue() == degree) {
                Integer[] range = m2.get(entry.getKey());
                result = Math.min(result, range[1] - range[0] + 1);
            }
        }
        return result;
    }
}