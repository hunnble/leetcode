class Solution(object):
    def generate(self, p, left, right, res):
        if left:
            self.generate(p + '(', left - 1, right, res)
        if right > left:
            self.generate(p + ')', left, right - 1, res)
        if not right:
            res.append(p)

    def generateParenthesisDfs(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate('', n, n, res)
        return res

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
