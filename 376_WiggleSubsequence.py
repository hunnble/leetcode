class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        counter, i, j = 1, 1, 0
        while i < len(nums):
            if nums[i] < nums[j]:
                counter += 1
                while i < len(nums) - 1 and nums[i + 1] <= nums[i]:
                    i += 1
            elif nums[i] > nums[j]:
                counter += 1
                while i < len(nums) - 1 and nums[i + 1] >= nums[i]:
                    i += 1
            i, j = i + 1, i

        return counter