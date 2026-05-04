class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        m = 0
        j = i + 1
        while j < len(prices):
            if j == len(prices):
                i += 1
                j = i + 1
            if prices[i] > prices[j]:
                i = j 
            elif prices[i] < prices[j]:
                m = max(m,prices[j] - prices[i])
            j += 1

        return m