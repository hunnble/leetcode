class Solution(object):
    def majorityElement(self, nums):
        """
        Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
        思路: 和169题一样，Moore计数法
        :type nums: List[int]
        :rtype: List[int]
        """
        n1, n2, c1, c2 = None, None, 0, 0
        for num in nums:
            if n1 == num:
                c1 += 1
            elif n2 == num:
                c2 += 1
            elif c1 == 0:
                n1, c1 = num, 1
            elif c2 == 0:
                n2, c2 = num, 1
            else:
                c1, c2 = c1 - 1, c2 - 1

        lenNums = len(nums)
        return [n for n in (n1, n2) if n is not None and nums.count(n) > lenNums / 3]