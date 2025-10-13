class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        MaxP = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            profit = prices[right] - prices[left]
            MaxP = max(MaxP, profit)
            right += 1
        return MaxP