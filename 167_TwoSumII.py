class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j, r = 0, len(numbers) - 1, numbers[0] + numbers[-1]
        while r != target:
            if r < target:
                i += 1
            else:
                j -= 1
            r = numbers[i] + numbers[j]

        return [i + 1, j + 1]
