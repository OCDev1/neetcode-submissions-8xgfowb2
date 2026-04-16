class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # relation:
        # f(n) = 1 + f(n-c) for all coins
        coins.sort()

        # build dp array with base cases
        arr = [0] * (amount + 1)

        arr[0] = 1  # one way to get 0

        for c in coins:
            for a in range(c, amount+1):
                arr[a] += arr[a-c]
        return arr[amount]