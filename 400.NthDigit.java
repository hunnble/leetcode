class Solution {
    public int findNthDigit(int n) {
        n -= 1;
        int digits = 1;
        int first = 1;
        while (n / 9 / digits / first >= 1) {
            n -= 9 * digits * first;
            digits += 1;
            first *= 10;
        }
        return (first + n / digits + "").charAt(n % digits) - '0';
    }
}
