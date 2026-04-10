class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # f(i,j) = if word1[i] == word2[j]: f(i-1,j-1)
        #          else: 1 + min(f(i-1,j-1), f(i,j-1), f(i-1,j))
        #     action cost^ + min(replace, delete char, insert char)

        arr = [ [0] * (len(word2)+1) for _ in range(len(word1)+1)]

        # base cases: if one word is longer than the other
        # we need to delete chars from the long one when the other is done
        for i in range(len(word1)+1):
            arr[i][0] = i   # word 2 out of chars
        for j in range(len(word2)+1):
            arr[0][j] = j   # word 1 out of chars

        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    arr[i][j] = arr[i-1][j-1]
                else:
                    arr[i][j] = 1 + min(arr[i-1][j-1], arr[i][j-1], arr[i-1][j])
        return arr[-1][-1]