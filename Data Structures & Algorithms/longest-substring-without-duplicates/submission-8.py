class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            while l<r and s[r] in seen: # Move left border of window until no duplicates
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            ans = max(ans,r-l+1)
        return ans