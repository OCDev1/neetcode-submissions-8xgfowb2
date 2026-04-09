class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # f(amount) = min(f(amount - coins[0]), f(amount - coins[1]), ...)
        arr = [amount + 1] * (amount + 1)   # why amount+1 in both? (amount + 1) is a sentinel value (tells us if cell has been reached)
                                            # [amount + 1] the extra cell is for the sentinel value
        # arr[i] - amount = i
        arr[0] = 0  # why not more base cases? look at the formula
                    # we compare only with amount (unlike n-1,n-2 etc.)

        for a in range(1,amount + 1):
            for c in coins:
                if a - c >= 0:  #why? if not we subtract too much - coin is too big
                    arr[a] = min(arr[a], 1 + arr[a-c]) # min(skip coin, use coin)

        if arr[amount] != amount+1: # why? if sentinel value hasn't changed - 
                                    # we cant reach this amount with the coins we have (cant reach the cell we want)
            return arr[amount]
        else:
            return -1