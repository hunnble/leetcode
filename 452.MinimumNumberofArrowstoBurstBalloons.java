import java.util.Arrays;

class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) {
            return 0;
        }
        Arrays.sort(points, (a, b) -> a[1] - b[1]);
        int arrowPos = points[0][1];
        int result = 1;
        for (int i = 1; i < points.length; i += 1) {
            if (arrowPos >= points[i][0]) {
                continue;
            }
            arrowPos = points[i][1];
            result += 1;
        }
        return result;
    }
}
