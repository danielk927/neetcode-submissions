class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix) - 1

        while l <= r: 
            m = (l + r) // 2
            rowMin = matrix[m][0]
            rowMax = matrix[m][-1]

            if target > rowMax:
                l = m + 1
            elif target < rowMin:
                r = m - 1
            else:
                lo = 0
                hi = len(matrix[m]) - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if matrix[m][mid] > target:
                        hi = mid - 1 
                    elif matrix[m][mid] < target:
                        lo = mid + 1 
                    else:
                        return True
                return False
        return False


