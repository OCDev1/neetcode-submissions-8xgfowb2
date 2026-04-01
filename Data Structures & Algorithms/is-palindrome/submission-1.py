class Solution:
    def isPalindrome(self, s: str) -> bool:
        start=0
        end=len(s)-1

        while start < end:
            while start < end and not self.isLetter(s[start]):
                start+=1
            while start < end and not self.isLetter(s[end]):
                end-=1
            if s[start].lower() != s[end].lower():
                return False
            start+=1
            end-=1
        return True

    def isLetter(self,c) -> bool:
        if(
            ord('A') <= ord(c) <=ord('Z') or
            ord('a') <= ord(c) <=ord('z') or
            ord('0') <= ord(c) <=ord('9')
        ):return True
        else: return False