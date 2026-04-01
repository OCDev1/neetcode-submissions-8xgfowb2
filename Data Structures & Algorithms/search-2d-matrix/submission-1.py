class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m,n = len(matrix), len(matrix[0])
        l,r = 0, n*m -1

        while l <= r:
            middle = (r+l)//2
            middle_val = matrix[middle // n][middle % n]

            if middle_val == target:
                return True
            elif middle_val < target:
                l = middle + 1
            else:
                r = middle - 1

        return False