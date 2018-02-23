import java.util.Arrays;

/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public int eraseOverlapIntervals(Interval[] intervals) {
        if (intervals.length <= 1) {
            return 0;
        }
        Arrays.sort(intervals, (a, b) -> a.end - b.end);
        int lowerBound = intervals[0].end;
        int result = 0;
        for (int i = 1; i < intervals.length; i += 1) {
            if (intervals[i].start < lowerBound) {
                result += 1;
            } else if (intervals[i].end > lowerBound) {
                lowerBound = intervals[i].end;
            }
        }
        return result;
    }
}
