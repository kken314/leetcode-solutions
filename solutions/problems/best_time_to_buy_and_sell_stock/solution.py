class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MinValBefore = float('inf')
        MaxProfit = 0
        for price in prices:
            profit = price - MinValBefore
            MaxProfit = max(MaxProfit, profit)
            if price < MinValBefore:
                MinValBefore = price
        return MaxProfit