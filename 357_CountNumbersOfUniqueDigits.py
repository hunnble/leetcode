class Solution(object):
    def f(self, k):
        if k == 1:
            return 10
        else:
            i, sum = 10, 9
            while i != (9 - k + 2):
                i -= 1
                sum *= i
        
        return sum
                
    def countNumbersWithUniqueDigits(self, n):
        """
        Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        r = 0
        for i in range(n):
            r += self.f(i + 1)
        
        return r