class Solution {
    public String reverseWords(String s) {
        String[] str = s.split(" ");
        for (int i = 0; i < str.length; i++) {
            str[i] = new StringBuilder(str[i]).reverse().toString();
        }
        StringBuilder result = new StringBuilder();
        for (String word : str) {
            result.append(word + " ");
        }
        return result.toString().trim();
    }
}
