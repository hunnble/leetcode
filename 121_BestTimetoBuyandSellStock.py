class Solution(object):
    def maxProfit(self, prices):
        """
        Say you have an array for which the ith element is the price of a given stock on day i.
        If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l <= 1:
            return 0
        dp = [0] * len(prices)
        r = prices[1] - prices[0]
        m = prices[0]
        for i in range(2, l):
            m = min(prices[i - 1], m)
            r = max(r, prices[i] - m)
        
        return r if r >= 0 else 0
        