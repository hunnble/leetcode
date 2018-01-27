class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int comp = 0;
        int tmp = x;
        while (tmp != 0) {
            comp = comp * 10 + tmp % 10;
            tmp /= 10;
        }
        return comp == x;
    }
}
