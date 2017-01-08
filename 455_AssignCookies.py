class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        r, i = 0, 0
        g.sort()
        s.sort()
        for si in s:
            if i == len(g):
                break
            else:
                if si >= g[i]:
                    r, i = r + 1, i + 1
        return r
