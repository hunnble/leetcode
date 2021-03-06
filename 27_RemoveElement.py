class Solution(object):
    def removeElement(self, nums, val):
        """
        Given an array and a value, remove all instances of that value in place and return the new length.
        Do not allocate extra space for another array, you must do this in place with constant memory.
        The order of elements can be changed. It doesn't matter what you leave beyond the new length.
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums.remove(nums[i])
                n -= 1
            else:
                i += 1
        
        return len(nums)