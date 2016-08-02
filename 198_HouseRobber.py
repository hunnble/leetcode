class Solution(object):
    def rob(self, nums):
        """
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
        Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]

        dp = [0] * l
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in xrange(2, l):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return max(dp)