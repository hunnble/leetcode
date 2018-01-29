class Solution {
    public boolean judgeSquareSum(int c) {
        if (c == 0) {
            return true;
        }
        for (int i = 0; i < Math.sqrt(c); i += 1) {
            if (Math.floor(Math.sqrt(c - i * i)) == Math.sqrt(c - i * i)) {
                return true;
            }
        }
        return false;
    }
}
