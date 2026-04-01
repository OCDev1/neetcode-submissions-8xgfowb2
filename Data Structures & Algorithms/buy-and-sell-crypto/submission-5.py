class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        max_profit = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            max_profit = max(max_profit, prices[r]-prices[l])
            
        return max_profit