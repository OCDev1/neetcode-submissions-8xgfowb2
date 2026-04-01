class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if h == len(piles):
                return max(piles)

        # function to check if the k can be a valid answer (not necessarily min)
        def does_satisfy(k, h)->bool:
            hours = 0
            piles_dup = piles
            
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours <= h
        
        # binary search for the answer
        l,r = 1, max(piles)
        while l <= r:    
            k = (r+l)//2
            if does_satisfy(k,h):
                ans = k
                r = k-1
            else:
                l = k+1
        
        return ans
        

        