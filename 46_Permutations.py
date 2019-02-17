class Solution(object):
    def pushChar(self, nums, curNums, res):
        for i in range(len(nums)):
            tmpNums = curNums[:]
            num = nums[i]
            tmpNums.append(num)
            nextNums = nums[:]
            nextNums.pop(i)
            if not nextNums:
                res.append(tmpNums)
            else:
                self.pushChar(nextNums, tmpNums, res)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.pushChar(nums, [], res)
        return res