class Solution {
    public int[] constructArray(int n, int k) {
        int[] result = new int[n];
        int p = 1;
        int q = n;
        int i = 0;
        while (k > 1) {
            result[i++] = k % 2 == 0 ? q -- : p++;
            k -= 1;
        }
        while (i < n) {
            result[i++] = p++;
        }
        return result;
    }
}