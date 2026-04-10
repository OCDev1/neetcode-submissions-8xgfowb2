class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # recurrance relation:
        # f(i,j) = 
        # if text1[i] == text2[j]: 1 + f(i-1,j-1) 
        # else: max(f(i-1,j),f(i,j-1))

        arr = [ [0]*(len(text2)+1) for i in range(len(text1)+1)]    # +1 for the empty string case

        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:  # same char, add 1 and move both ptrs
                    arr[i][j] = 1 + arr[i-1][j-1]
                else:   # mismatch, return max of moving each ptr back
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        
        return arr[-1][-1]