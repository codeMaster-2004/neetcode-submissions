class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c = 0
        check = False
        for r in range(len(matrix)):
            if (target >= matrix[r][c]) and (target <= matrix[r][len(matrix[r]) - 1]):
                l = 0
                right = len(matrix[r]) - 1
                while l <= right:
                    m = (l+right) // 2
                    if target == matrix[r][m]:
                        return True
                    elif matrix[r][m] > target:
                        right = m - 1
                    elif matrix[r][m] < target:
                        l = m + 1


        return check 