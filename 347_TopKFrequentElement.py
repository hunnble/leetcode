class Solution(object):
    def heapAdjust(self, n, i, l, f):
        t = n[i]
        j = 2 * i
        while j <= l:
            if j < l and f[n[j]] > f[n[j + 1]]:
                j += 1
            if f[t] <= f[n[j]]:
                break
            n[i] = n[j]
            i = j
            j *= 2

        n[i] = t

    def topKFrequent(self, nums, k):
        """
        Given a non-empty array of integers, return the k most frequent elements.
        思路：堆排序
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = dict()
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        n = list(freq)
        l = len(n)

        i = l // 2
        while i >= 0:
            self.heapAdjust(n, i, l - 1, freq)
            i -= 1

        i = l - 1
        while i >= 0:
            t = n[0]
            n[0] = n[i]
            n[i] = t
            self.heapAdjust(n, 0, i - 1, freq)
            i -= 1

        return n[0:k]