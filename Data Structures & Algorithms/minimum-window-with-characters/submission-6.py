class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if not s:
            return ""

        ans = ""
        need = Counter(t)
        have = defaultdict(int)

        formed = 0
        required = len(need)
        l = 0

        for r in range(len(s)):
            have[s[r]] += 1
            if s[r] in need and have[s[r]] == need[s[r]]:
                formed += 1
            
            while formed == required:
                window = s[l:r+1]
                if not ans or len(window) < len(ans):
                    ans = window
                # Update tracking for the left border shrinking
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        
        return ans