import java.util.Arrays;

class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] tmp = new int[26];
        for (char t : tasks) {
            tmp[t - 'A'] += 1;
        }
        Arrays.sort(tmp);
        int i = 25;
        while (i >= 0 && tmp[i] == tmp[25]) {
            i -= 1;
        }
        return Math.max(tasks.length, (tmp[25] - 1) * (n + 1) + 25 - i);
    }
}