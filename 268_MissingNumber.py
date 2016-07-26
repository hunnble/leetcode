class Solution(object):
    def missingNumber(self, nums):
        """
        Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
        For example,
        Given nums = [0, 1, 3] return 2.
        Note:
        Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        return (l + 1) * l / 2 - sum(nums)