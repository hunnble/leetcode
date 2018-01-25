class Solution {
    public boolean isPerfectSquare(int num) {
        int tmp = num;
        while (tmp * tmp > num) {
            tmp = (tmp + num / tmp) >> 1;
        }
        return tmp * tmp == num;
    }
}
