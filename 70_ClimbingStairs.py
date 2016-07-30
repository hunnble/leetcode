class Solution(object):
    def climbStairs(self, n):
        """
        You are climbing a stair case. It takes n steps to reach to the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        :type n: int
        :rtype: int
        """
        pre, i, sum = 0, 0, 1
        while i < n:
            t = sum
            sum += pre
            pre = t
            i += 1
        
        return sum
        