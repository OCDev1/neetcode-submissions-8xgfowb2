class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = [amount + 1] * (amount + 1)
        print(a)

        # base case
        a[0] = 0

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    a[i] = min(a[i-coins[j]] + 1, a[i])
        res = a[amount] if a[amount] != amount + 1 else -1 
        return res