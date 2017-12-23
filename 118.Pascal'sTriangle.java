import java.util.ArrayList;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        ArrayList<Integer> row = new ArrayList<Integer>();
        for (int i = 0; i < numRows; i += 1) {
            row.add(0, 1);
            for (int j = 1; j < row.size() - 1; j += 1) {
                row.set(j, row.get(j) + row.get(j + 1));
            }
            result.add(new ArrayList<Integer>(row));
        }
        return result;
    }
}