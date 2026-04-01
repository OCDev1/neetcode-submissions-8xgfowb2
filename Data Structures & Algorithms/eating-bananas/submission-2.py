class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find biggest pile in piles:
        max_pile = 0
        for pile in piles:
            max_pile=max(max_pile,pile)
        
        # function that checks if eat rate is sufficient
        def eatpiles(temp_piles: List[int], hours: int, k: int) -> bool:
            for i in range(len(temp_piles)):
                    hours-= math.ceil(temp_piles[i]/k) # subtract hours needed to finish pile
            # if we havent passed the given time h - return true
            return hours >= 0
        
        min_rate = max_pile
        # binary search for the min rate
        l,r=1,max_pile
        while l <= r:
            hours = h
            middle = (l+r) // 2
            if eatpiles(piles, hours, middle):
                min_rate=min(min_rate, middle)
                r = middle - 1
            else:
                l = middle + 1

        return min_rate