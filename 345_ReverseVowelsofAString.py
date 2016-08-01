class Solution(object):
    def reverseVowels(self, s):
        """
        Write a function that takes a string as input and reverse only the vowels of a string.
        :type s: str
        :rtype: str
        """
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        s = list(s)
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            i1, i2 = s[p1] in vowels, s[p2] in vowels
            if i1 and i2:
                s[p1], s[p2] = s[p2], s[p1]
                p1, p2 = p1 + 1, p2 - 1
            elif not i1 and not i2:
                p1, p2 = p1 + 1, p2 - 1
            elif i1:
                p2 -= 1
            else:
                p1 += 1
        
        return ''.join(s)