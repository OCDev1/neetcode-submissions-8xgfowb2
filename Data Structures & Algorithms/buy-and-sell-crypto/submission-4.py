class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        max_profit = 0

        for win_size in range(2, len(prices)+1):
            start = 0
            while start+win_size <= len(prices):
                max_profit = max(max_profit, prices[start+win_size-1]-prices[start])
                start +=1
        
        return max_profit