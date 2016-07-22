class Solution(object):
    def majorityElement(self, nums):
        """
        Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
        You may assume that the array is non-empty and the majority element always exist in the array.
        思路: https://discuss.leetcode.com/topic/6249/c-solution-o-n-computation-o-1-space-the-problem-can-be-extended-to-n-k-situation
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)):
            if counter == 0:
                result = nums[i]
                counter += 1
            elif result == nums[i]:
                counter += 1
            else:
                counter -= 1

        return result