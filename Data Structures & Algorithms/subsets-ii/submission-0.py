class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        counters = []   # counts for all sets in res, to detect duplicates
        cur_subset = []

        def dfs(i):
            if i >= len(nums):
                cur_count = collections.Counter(cur_subset)
                if cur_count not in counters:
                    counters.append(cur_count)
                    res.append(cur_subset.copy())   # we've reached a leaf, add it it to result
                return
            
            cur_subset.append(nums[i])  # add nums[i]
            dfs(i+1)    # explore this option
            cur_subset.pop()    # remove nums[i]
            dfs(i+1)    # explore this option

        dfs(0)
        return res
            