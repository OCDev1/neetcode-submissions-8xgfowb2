class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []       
        cur_subset = []
        
        def helper(i: int) -> None:
            if i >= len(nums):
                res.append(cur_subset.copy())
                return

            # add copy with and without i'th member and recurse
            cur_subset.append(nums[i])
            helper(i+1)
            cur_subset.pop()
            helper(i+1)
            return
        
        helper(0)
        return res



