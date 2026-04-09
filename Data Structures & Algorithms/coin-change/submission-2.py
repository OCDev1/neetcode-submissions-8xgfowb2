class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # f(amount) = min(f(amount - coins[0]), f(amount - coins[1]), ...)
        arr = [amount + 1] * (amount + 1)   # why amount+1 in both?

        arr[0] = 0  # why not more base cases?

        for a in range(1,amount + 1):
            for c in coins:
                if a - c >= 0:
                    arr[a] = min(arr[a], 1 + arr[a-c])

        if arr[amount] != amount+1:
            return arr[amount]
        else:
            return -1