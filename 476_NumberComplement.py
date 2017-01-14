class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(num)
        nnum = []
        for i in range(2, len(num)):
            tmp = '0' if num[i] == '1' else '1'
            nnum.append(tmp)

        return int(''.join(nnum), 2)
