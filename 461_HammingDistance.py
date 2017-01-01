class Solution(object):
    def hammingDistance(self, x, y):
        """
        The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
        Given two integers x and y, calculate the Hamming distance.
        :type x: int
        :type y: int
        :rtype: int
        """
        return str(bin(x ^ y))[2:].count('1')
