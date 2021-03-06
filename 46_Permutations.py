class Solution(object):
    def dfs(self, nums, curNums, res):
        for i in range(len(nums)):
            tmpNums = curNums[:] + [nums[i]]
            nextNums = nums[0:i] + nums[i + 1:]
            if not nextNums:
                res.append(tmpNums)
            else:
                self.dfs(nextNums, tmpNums, res)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res

    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return map(list, itertools.permutations(nums))