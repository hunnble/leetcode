import java.awt.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(result, new ArrayList<Integer>(), nums, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> tmp, int[] nums, int start) {
        result.add(new ArrayList<>(tmp));
        for (int i = start; i < nums.length; i += 1) {
            tmp.add(nums[i]);
            backtrack(result, tmp, nums, i + 1);
            tmp.remove(tmp.size() - 1);
        }
    }
}