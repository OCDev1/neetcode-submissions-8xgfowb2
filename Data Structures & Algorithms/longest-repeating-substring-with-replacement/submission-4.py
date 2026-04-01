class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0

        r,l = 0,0
        ans = 1
        # find the longest substring from all options of replacement letters
        for i in range(26):
            cur_letter = ord('A') + i
            l,r = 0,0
            count = k
            # the sliding window
            while r < len(s):
                if ord(s[r]) == cur_letter:
                    ans = max(ans, r-l+1)
                    r+=1    # expand window
                elif s[r] != cur_letter and count > 0:
                    count-=1    # use a replacement letter
                    ans = max(ans, r-l+1)
                    r+=1    # expand window
                else:       # no replacements left
                    if ord(s[l]) == cur_letter:
                        l+=1
                    else:
                        l+=1
                        count+=1
        
        return ans