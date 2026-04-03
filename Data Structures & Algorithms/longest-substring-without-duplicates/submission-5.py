class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            while l<r and s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            r+=1
            ans = max(ans,r-l)
        return ans