class Solution {
    public int monotoneIncreasingDigits(int N) {
        if (N <= 9) {
            return N;
        }
        char[] digits = String.valueOf(N).toCharArray();
        int mark = digits.length;
        for (int i = digits.length - 1; i > 0; i -= 1) {
            if (digits[i] < digits[i - 1]) {
                mark = i - 1;
                digits[i - 1] -= 1;
            }
        }
        for (int i = mark + 1; i < digits.length; i += 1) {
            digits[i] = '9';
        }
        return Integer.parseInt(new String(digits));
    }
}
