class Solution {
    public boolean judgeCircle(String moves) {
        int x = 0;
        int y = 0;
        for (char ch : moves.toCharArray()) {
            if (ch == 'U') {
                x += 1;
            } else if (ch == 'D') {
                x -= 1;
            } else if (ch == 'L') {
                y -= 1;
            } else {
                y += 1;
            }
        }
        return x == 0 && y == 0;
    }
}
