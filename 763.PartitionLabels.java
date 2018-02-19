import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> partitionLabels(String S) {
        if (S == null || S.length() == 0) {
            return null;
        }
        List<Integer> result = new ArrayList<Integer>();
        int start = 0;
        int end = 0;
        int[] map = new int[26];
        for (int i = 0; i < S.length(); i += 1) {
            map[S.charAt(i) - 'a'] = i;
        }
        for (int i = 0; i < S.length(); i += 1) {
            end = Math.max(end, map[S.charAt(i) - 'a']);
            if (end == i) {
                result.add(end - start + 1);
                start = i + 1;
            }
        }
        return result;
    }
}
