class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result, tmp = 0, 1
        if len(A) < 3:
            return 0
        flag = A[1] - A[0]
        for i in range(2, len(A)):
            if A[i] - A[i-1] == flag:
                tmp += 1
            else:
                result += tmp * (tmp - 1) / 2
                flag = A[i] - A[i-1]
                tmp = 1
        result += tmp * (tmp - 1) / 2

        return result
