import math

class Solution(object):
    def integerBreak(self, n):
        """
        Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
        For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
        Note: You may assume that n is not less than 2 and not larger than 58.
        思路: https://www.h5jun.com/post/integer-break.html
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n % 3 == 0:
            return int(math.pow(3, n / 3))
        elif n % 3 == 1:
            return int(4 * math.pow(3, (n - 1) / 3 - 1))
        else:
            return int(2 * math.pow(3, n / 3))