from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_count = Counter(t)
        s_count = Counter()
        
        l = 0
        matches = 0
        min_len = float('inf')
        res = ""
        
        for r in range(len(s)):
            # Add the current character to s_count
            s_count[s[r]] += 1
            
            # Check if this character is in t and if we have matched the required number of this character
            if s_count[s[r]] == t_count[s[r]]:
                matches += 1
            
            # Once we have matched all the characters in t, try to shrink the window
            while matches == len(t_count):
                # Check if the current window is smaller than the previous minimum
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1]
                
                # Remove the leftmost character and update the match count
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    matches -= 1
                l += 1
        
        return res
