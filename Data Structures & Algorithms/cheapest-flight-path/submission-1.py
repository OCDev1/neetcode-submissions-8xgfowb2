class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # initialization
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):  # run k times (for k stops)
            tmpPrices = prices.copy()

            for src1, dest, price in flights:  # iterate over edges (flights) list
                if prices[src1] == float("inf"): # haven't reached this node yet
                    continue
                if prices[src1] + price < tmpPrices[dest]:    # if newly discovered path is shorter-update to it
                    tmpPrices[dest] = prices[src1] + price

            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]