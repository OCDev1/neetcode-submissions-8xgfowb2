class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix), len(matrix[0])
        top,bot = 0,rows-1

        # find the correct row (array)
        while top <= bot:
            row = (top+bot) // 2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row +1
            else:
                break
        l,r = 0,cols-1
        while l <= r:
            middle = (r+l)//2
            middle_val = matrix[row][middle]

            if middle_val == target:
                return True
            elif middle_val < target:
                l = middle + 1
            else:
                r = middle - 1

        return False