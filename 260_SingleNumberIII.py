class Solution(object):
    def singleNumber(self, nums):
        """
        Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
        For example:
        Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = {}
        result = []
        for i in range(0, len(nums)):
            if tmp.get(nums[i], 0) is 0:
                tmp.setdefault(nums[i], 1)
            else:
                del tmp[nums[i]]

        for key in tmp:
            result.append(key)

        return result
