class Solution {
    public int countPrimes(int n) {
        boolean[] isPrimes = new boolean[n];
        int count = 0;
        for (int i = 2; i < n; i += 1) {
            if (isPrimes[i]) {
                continue;
            }
            count += 1;
            for (int j = i; j < n; j += i) {
                isPrimes[j] = true;
            }
        }
        return count;
    }
}
