class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        l, r = 1, 1
        for i in range(len(nums)):
            result[i] *= l
            l *= nums[i]
            result[len(nums) - i - 1] *= r
            r *= nums[len(nums) - i - 1]

        return result