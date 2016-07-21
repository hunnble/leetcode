class Solution(object):
    def titleToNumber(self, s):
        """
        Given a column title as appear in an Excel sheet, return its corresponding column number.
        :type s: str
        :rtype: int
        """
        digit = 1
        result = 0
        while(s != ''):
            result += (ord(s[-1]) - 64) * digit
            digit *= 26
            s = s[:-1]

        return result