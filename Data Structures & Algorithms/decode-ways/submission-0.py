class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        # init dp array
        a = [0] * len(s)
        
        # base case
        if s[0] != "0":
            a[0] = 1

        for i in range(1, len(s)):
            if s[i] != "0":
                a[i] = a[i-1]

            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                a[i] += (a[i - 2] if i >=2 else 1)
            
        print(a)
        
        return a[-1]