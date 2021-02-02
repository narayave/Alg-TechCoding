
# Leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        maxp = 0
        while j <= len(prices) - 1:
            if prices[j] > prices[i]:
                maxp += prices[j] - prices[i]
            i += 1
            j += 1
        return maxp