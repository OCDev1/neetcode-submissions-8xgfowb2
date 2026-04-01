class Solution:
    def partition(self, s: str) -> List[List[str]]:
        all_parts = []
        cur_part = []

        def is_palindrome(string,l,r) -> bool:
            while l<r:
                if string[l] == string[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True

        def dfs(i):
            #base case: we reached the end of the string
            if i >= len(s):      
                all_parts.append(cur_part.copy())
                return
            #we have a partition up to index j, 
            #now we look for the next palindrome starting at j+1:
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    cur_part.append(s[i:j+1]) #adding the current palindrome to the partition
                    dfs(j+1)                #looking for the next palindrome
                    cur_part.pop()  #this is a clean up for the next iteration in the loop

        dfs(0)
            
        return all_parts

            
