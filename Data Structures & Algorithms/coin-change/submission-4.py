class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # f(amount) = 1 + min{f(amount-coins[0]),f(amount - coins[1],f(...),...}
        if not amount:
            return 0
        
        # dp array
        arr = [float('inf')] * (amount+1)
        # base case
        arr[0] = 0

        for i in range(amount):
            for c in coins:
                if i+c > amount:
                    continue
                arr[i+c] = min(1 + arr[i], arr[i+c])    # track min amount of coins needed to reach

        if arr[amount] == float('inf'):
            return -1
        else:
            return int(arr[amount])