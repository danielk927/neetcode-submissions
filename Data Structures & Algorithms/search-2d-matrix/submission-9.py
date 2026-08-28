class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix) - 1 

        while l <= r: 
            m = (l + r) // 2 
            if matrix[m][0] > target: 
                r = m - 1 
            elif matrix[m][-1] < target: 
                l = m + 1 
            else: 
                left = 0 
                right = len(matrix[0]) - 1

                while left <= right: 
                    mid = (left + right) // 2 
                    if matrix[m][mid] < target: 
                        left = mid + 1 
                    elif matrix[m][mid] > target: 
                        right = mid - 1 
                    else: 
                        return True 
                return False
        return False 