class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        lowest = prices[0]

        for sell_day in range(1,len(prices)):
            lowest = min(lowest, prices[sell_day-1])
            ans = max(ans, prices[sell_day] - lowest)

        return ans