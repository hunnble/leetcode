class Solution(object):
    def generate(self, numRows):
        """
        Given numRows, generate the first numRows of Pascal's triangle.
        :type numRows: int
        :rtype: List[List[int]]
        """
        r = []
        for i in xrange(numRows):
            if i == 0:
                r.append([1])
            else:
                t = [1]
                for j in xrange(len(r[i-1]) - 1):
                    t.append(r[i-1][j] + r[i-1][j+1])
                t.append(1)
                r.append(t)
        
        return r