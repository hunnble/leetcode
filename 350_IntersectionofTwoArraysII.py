class Solution(object):
    def intersect(self, nums1, nums2):
        """
        Given two arrays, write a function to compute their intersection.
        Example:
        Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
        Note:
        Each element in the result should appear as many times as it shows in both arrays.
        The result can be in any order.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        result = []
        i, j = 0, 0
        while i != len(nums1) and j != len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i, j = i + 1, j + 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result