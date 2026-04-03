class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        i,j = 0, len(s)-1
    
        while i<j:
            # Handle non alphaNumeric chars
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            
            # Actual comparison
            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True