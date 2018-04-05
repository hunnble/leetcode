/**
 * binary indexed tree
 */
class NumArray {
    private int[] nums;
    private int[] BIT;
    private int len;

    public NumArray(int[] nums) {
        this.nums = nums;
        len = nums.length;
        BIT = new int[len + 1];
        for (int i = 0; i < len; i += 1) {
            init(i, nums[i]);
        }
    }

    public void init(int i, int val) {
        i += 1;
        while (i <= len) {
            BIT[i] += val;
            i += (i & -i);
        }
    }

    public void update(int i, int val) {
        int diff = val - nums[i];
        nums[i] = val;
        init(i, diff);
    }

    public int getSum(int i) {
        int sum = 0;
        i += 1;
        while (i > 0) {
            sum += BIT[i];
            i -= (i & -i);
        }
        return sum;
    }

    public int sumRange(int i, int j) {
        return getSum(j) - getSum(i - 1);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
