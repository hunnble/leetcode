class Solution(object):
    def plusOne(self, digits):
        """
        Given a non-negative number represented as an array of digits, plus one to the number.
        The digits are stored such that the most significant digit is at the head of the list.
        :type digits: List[int]
        :rtype: List[int]
        """
        p, d = len(digits) - 1, False
        for p in xrange(len(digits)-1, -1, -1):
            digits[p] += 1
            if digits[p] < 10:
                return digits
            else:
                digits[p] -= 10
        digits.insert(0, 1)
        
        return digits