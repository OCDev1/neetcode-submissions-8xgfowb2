class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()

        def helper(i, cur):
            if sum(cur) == target:
                self.res.append(cur.copy())
                return
            
            if sum(cur) >= target or i == len(candidates):
                return

            cur.append(candidates[i])
            helper(i+1, cur)
            cur.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1, cur)
        
        helper(0, [])
        return self.res

