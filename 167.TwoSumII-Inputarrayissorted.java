class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length - 1;
        int sum = numbers[i] + numbers[j];
        while (sum != target) {
            if (sum < target) {
                i += 1;
            } else {
                j -= 1;
            }
            sum = numbers[i] + numbers[j];
        }
        int[] result = new int[2];
        result[0] = i + 1;
        result[1] = j + 1;
        return result;
    }
}