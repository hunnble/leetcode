class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        if (timeSeries.length == 0 || duration == 0) {
            return 0;
        }
        int result = 0;
        int start = timeSeries[0];
        int end = start + duration;
        for (int i = 1; i < timeSeries.length; i += 1) {
            if (timeSeries[i] > end) {
                result += end - start;
                start = timeSeries[i];
            }
            end = timeSeries[i] + duration;
        }
        result += end - start;
        return result;
    }
}