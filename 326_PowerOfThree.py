class Solution(object):
    def isPowerOfThree(self, n):
        """
        Given an integer, write a function to determine if it is a power of three.
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
            
        while n % 3 == 0 and n != 1:
            n = n / 3
        
        return n == 1