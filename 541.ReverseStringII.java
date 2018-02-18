class Solution {
    public String reverseStr(String s, int k) {
        char[] arr = s.toCharArray();
        int len = arr.length;
        int i = 0;
        while (i < len) {
            int j = Math.min(i + k - 1, len - 1);
            swap(arr, i, j);
            i += 2 * k;
        }
        return String.valueOf(arr);
    }

    private void swap(char[] arr, int i, int j) {
        while (i < j) {
            char tmp = arr[i];
            arr[i++] = arr[j];
            arr[j--] = tmp;
        }
    }
}
