class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        myset = set()   # to check for duplicates
        l,r=0,1
        ans = 1     # min substring length

        myset.add(s[l])
        while r < len(s):
            if s[r] in myset:
                # moving to the next window
                myset.remove(s[l])
                l += 1

            else:
                myset.add(s[r])
                ans = max(ans, r-l+1)
                r+=1
        return ans
