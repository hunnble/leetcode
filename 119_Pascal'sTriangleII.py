class Solution(object):
    def getRow(self, rowIndex):
        """
        Given an index k, return the kth row of the Pascal's triangle.
        For example, given k = 3,
        Return [1,3,3,1].
        Note: Could you optimize your algorithm to use only O(k) extra space?
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        r = [1, 1]
        for i in xrange(rowIndex - 1):
            for j in xrange(len(r) - 1):
                r[j] = r[j] + r[j + 1]
            r.insert(0, 1)
        
        return r