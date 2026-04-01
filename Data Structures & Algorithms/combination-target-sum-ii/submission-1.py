class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()

        def helper(i, cur, goal):
            if goal == target:
                self.res.append(cur.copy())
                return
            
            if goal >= target or i == len(candidates):
                return

            # this part will add all valid combos with duplicate numbers
            cur.append(candidates[i])
            helper(i+1, cur, goal + candidates[i])
            cur.pop()

            # this part will add all valid combos without duplicate numbers
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1, cur, goal)
        
        helper(0, [], 0)
        return self.res

