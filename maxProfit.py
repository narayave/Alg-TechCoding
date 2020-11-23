class Solution:

    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    def maxProfit(self, prices: List[int]) -> int:

        if prices == []:
            return 0

        minp = prices[0]
        profit = 0

        for i in prices:

            if i < minp:
                minp = i

            if i >= minp:
                localprice = i - minp

                if localprice > profit:
                    profit = localprice

        return profit
