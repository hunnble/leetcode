class Solution(object):
    def isPowerOfFour(self, num):
        """
        Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
        :type num: int
        :rtype: bool
        """
        binNum = bin(num)
        return num > 0 and binNum.count('1') == 1 and len(binNum) % 2 == 1