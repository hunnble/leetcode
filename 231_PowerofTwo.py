class Solution(object):
    def isPowerOfTwo(self, n):
        """
        Given an integer, write a function to determine if it is a power of two.
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
            
        return bin(n).count('1') == 1