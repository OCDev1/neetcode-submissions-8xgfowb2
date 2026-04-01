class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []       
        cur_subset = []
        
        def helper(i: int) -> None:
            if i >= len(nums):  # add to res only when we reach bottom of recursion to avoid duplicates
                res.append(cur_subset.copy())
                return

            # recursion with and without i'th member
            cur_subset.append(nums[i])
            helper(i+1) # with i'th member, this call goes all the way down and adds all subsets in this path before changing cur_subset
            cur_subset.pop()
            helper(i+1) # without i'th member
            return
        
        helper(0)
        return res



