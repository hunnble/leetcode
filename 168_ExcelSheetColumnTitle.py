class Solution(object):
    def convertToTitle(self, n):
        """
        Given a positive integer, return its corresponding column title as appear in an Excel sheet.
        :type n: int
        :rtype: str
        """
        result = ''
        while(n != 0):
            r = n % 26
            if r == 0:
                r = 26
            n = (n - r) / 26
            result = chr(r + 64) + result

        return result
