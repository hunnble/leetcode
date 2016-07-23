class Solution(object):
    def containsDuplicate(self, nums):
        """
        Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(list(set(nums)))