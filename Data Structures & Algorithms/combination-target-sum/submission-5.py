class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur_combo = []
        def dfs(i):
            if i >= len(nums) or sum(cur_combo) > target:
                return
            elif sum(cur_combo) == target:
                ans.append(cur_combo.copy())
                return

            cur_combo.append(nums[i])
            dfs(i)
            cur_combo.pop()
            dfs(i+1)

        dfs(0)
        return ans