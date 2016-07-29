class Solution(object):
    def isHappy(self, n):
        """
        Write an algorithm to determine if a number is "happy".
        A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
        :type n: int
        :rtype: bool
        """
        h= {}
        while not h.get(str(n), None):
            h[str(n)], s = 1, 0
            while n >= 1:
                r = n % 10
                s += r * r
                n = n // 10
            n = s
        
        return n == 1