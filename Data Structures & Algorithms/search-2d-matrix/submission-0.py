class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(arr: List[int], target) -> bool:
            if not arr:
                return False
            middle = len(arr)//2
            if arr[middle] == target:
                return True
            elif arr[middle] < target:
                return binSearch(arr[middle+1:],target)
            else:
                return binSearch(arr[:middle],target)

        if not matrix:
            return False

        middle_arr = len(matrix)//2

        if matrix[middle_arr][0] > target:
            return self.searchMatrix(matrix[:middle_arr], target)
        
        elif matrix[middle_arr][len(matrix[middle_arr])-1] < target:
            return self.searchMatrix(matrix[middle_arr + 1:], target)

        else:
            return binSearch(matrix[middle_arr], target)