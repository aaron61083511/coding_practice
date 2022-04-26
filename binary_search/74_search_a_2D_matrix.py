class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        right = n_rows * n_cols - 1
        
        while left <= right:
            mid = left + (right - left)//2
            mid_value = matrix[mid//n_cols][mid%n_cols]
            if mid_value == target:
                return True
            elif mid_value > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
