class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #f(m,n) = 1 + f(m-1,n) + f(m,n-1)
        rows,cols = m,n
        arr = [ [1] * cols for r in range(rows)]

        # base cases:
        # covered in init of arr

        for r in range(1,rows):
            for c in range(1,cols):
                arr[r][c] = arr[r-1][c] + arr[r][c-1]
        
        # ans is in bottom right corner
        return arr[-1][-1]