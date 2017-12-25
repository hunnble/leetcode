import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int index = -1;
        for (int i = 0; i < nums.length; i += 1) {
            index = map.getOrDefault(nums[i], -1);
            if (index != -1 && Math.abs(index - i) <= k) {
                return true;
            }
            map.put(nums[i], i);
        }
        return false;
    }
}