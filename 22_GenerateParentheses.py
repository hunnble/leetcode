class Solution(object):
    def generate(self, p, left, right, res):
        if left:
            self.generate(p + '(', left - 1, right, res)
        if right > left:
            self.generate(p + ')', left, right - 1, res)
        if not right:
            res.append(p)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate('', n, n, res)
        return res
