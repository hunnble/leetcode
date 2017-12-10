class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int len = bits.length;
        int ones = 0;
        for (int i = len - 2; i >= 0 && bits[i] == 1; i -= 1) {
            ones += 1;
        }
        return ones % 2 != 1;
    }
}