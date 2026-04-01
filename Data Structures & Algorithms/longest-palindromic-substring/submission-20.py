class Solution:
    def longestPalindrome(self, s: str) -> str:
        # this stores the final answer
        start, fin = 0, 0
        for i in range(len(s)):
            l,r = i, i
            
            while(l>=0 and r<len(s)):
                if s[l] == s[r]:
                    # update longest palindrome
                    if (fin - start < r-l):
                        fin = r
                        start = l
                    l-=1
                    r+=1
                else:
                    break
        for i in range(len(s) - 1):
            l,r = i, i+1
            if s[l] == s[r]:
                    # update longest palindrome
                    if (fin - start <= r-l):
                        fin = r
                        start = l
            while(l>=0 and r<len(s)):
                if s[l] == s[r]:
                    # update longest palindrome
                    if (fin - start <= r-l):
                        fin = r
                        start = l
                    l-=1
                    r+=1
                else:
                    break
        return s[start:fin+1]

