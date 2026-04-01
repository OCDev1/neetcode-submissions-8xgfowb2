class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        myset = set()   # to check for duplicates
        l,r=0,1
        ans = 1     # min substring length

        while r < len(s):
            myset.add(s[l])

            if s[r] in myset:
                ans = max(ans, r-l)
                # moving to the next window
                l+=1
                r = l+1
                # empty hash set
                myset = set()
            else:
                myset.add(s[r])
                ans = max(ans, r-l+1)
                r+=1

        return ans
