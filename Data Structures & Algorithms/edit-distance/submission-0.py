class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        a = [ [float("inf")] * (len(word2)+1) for _ in range(len(word1)+1)]

        a[0][0]=0

        for i in range(1, len(word1)+1):
            a[i][0]= i
 
        for j in range(1, len(word2)+1):
            a[0][j]= j
        
        for i in range(1, len(word1)+1,):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    a[i][j] = a[i-1][j-1]
                else:
                    a[i][j] = min(a[i-1][j-1]+1 , a[i-1][j]+1 , a[i][j-1]+1)
        
        return a[len(word1)][len(word2)]