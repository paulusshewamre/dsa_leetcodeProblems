class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1

        while top <= bottom:
            m = (top + bottom) // 2
            if matrix[m][0] < target and matrix[m][len(matrix[m])-1] > target:
                break
            elif matrix[m][0] > target:
                bottom = m - 1
            else:
                top = m + 1
        
        row = (top + bottom) // 2
        s = 0
        e = len(matrix[row])-1

        while s <= e:
            m = (s + e) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                s = m + 1
            else:
                e = m - 1
        
        return False