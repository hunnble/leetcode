class Solution(object):
    def maxSubArray(self, nums):
        """
        Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
        For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
        the contiguous subarray [4,−1,2,1] has the largest sum = 6.
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dp = [0] * l
        dp[0] = nums[0]
        for i in range(1, l):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        endp = max(dp)
        
        return endp