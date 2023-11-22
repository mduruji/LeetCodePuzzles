class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res=0
        left = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res