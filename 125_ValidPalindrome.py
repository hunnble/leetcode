class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        s = list(filter(str.isalnum, s.lower()))
        return s == s[::-1]