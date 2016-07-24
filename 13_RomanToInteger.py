class Solution(object):
    def romanToInt(self, s):
        """
        Given a roman numeral, convert it to an integer.
        Input is guaranteed to be within the range from 1 to 3999.
        :type s: str
        :rtype: int
        """
        gladiators = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        stat = 'I'
        num = 0
        s = s[::-1]
        for key in s:
            if gladiators[key] >= gladiators[stat]:
                num += gladiators[key]
            else:
                num -= gladiators[key]
            stat = key

        return num