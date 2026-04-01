class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        counters = []   # counts for all sets in res, to detect duplicates
        cur_subset = []

        def dfs(i):
            if i >= len(nums): # we've reached a leaf, maybe add it to result
                cur_count = collections.Counter(cur_subset) # create a count for the current set (O(n))
                if cur_count not in counters:   # check if exists a set with a count like this, if not add the set and it's count
                    counters.append(cur_count)
                    res.append(cur_subset.copy())
                return
            
            cur_subset.append(nums[i])  # add nums[i]
            dfs(i+1)    # explore this option
            cur_subset.pop()    # remove nums[i]
            dfs(i+1)    # explore this option

        dfs(0)
        return res
            