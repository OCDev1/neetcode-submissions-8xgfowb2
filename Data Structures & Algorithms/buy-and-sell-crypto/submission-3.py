class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        max_profit = 0

        for win_size in range(2, len(prices)+1):
            start = 0
            while start+win_size <= len(prices):
                for i in range(start, start+win_size):
                    max_profit = max(max_profit, prices[i]-prices[start])
                start +=1
        
        return max_profit