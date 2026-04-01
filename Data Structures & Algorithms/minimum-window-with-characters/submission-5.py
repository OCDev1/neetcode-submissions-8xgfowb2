class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # edge cases
        if t == "":
            return ""

        matches = 0
        min_len = float('inf')
        res = ""
        t_count = Counter(t)
        s_count = Counter()
        l=0
        
        for r in range(len(s)):
            s_count[s[r]] += 1
            
            if s_count[s[r]] == t_count[s[r]]:
                matches += 1
            while matches == len(t_count):
                if (r-l+1) < min_len:
                    min_len = (r-l+1)
                    res = s[l:r+1]
                #shrink the window from the left
                s_count[s[l]] -= 1
                # update matches
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:   # only if we got rid of a letter in t, decrement matches
                    matches -= 1
                l += 1
        return res

