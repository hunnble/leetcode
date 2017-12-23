import java.util.ArrayList;

class Solution {
    public List<Integer> getRow(int rowIndex) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < rowIndex + 1; i += 1) {
            result.add(0, 1);
            for (int j = 1; j < result.size() - 1; j += 1) {
                result.set(j, result.get(j) + result.get(j + 1));
            }
        }
        return result;
    }
}