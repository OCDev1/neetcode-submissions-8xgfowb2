class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur_perm, remaining):
            if not remaining:   # if we added all nums to our permutation then stop
                res.append(cur_perm.copy()) # add the permutation to the result
                return

            for i in range(len(remaining)):     # loop for all numbers to try as the next element
                cur_perm.append(remaining[i])   # add current to permutation
                backtrack(cur_perm.copy(), remaining[:i]+remaining[i+1:])   # explore this path, we also removed i'th num from remaining
                cur_perm.pop()  # take this number out so we can try other numbers


        backtrack([], nums.copy())
        return res