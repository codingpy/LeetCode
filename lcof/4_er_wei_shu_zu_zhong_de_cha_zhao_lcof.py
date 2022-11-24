class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        n = len(matrix)
        m = len(matrix[0])

        i = n - 1
        j = 0

        while 0 <= i and j < m:
            num = matrix[i][j]

            if num > target:
                i -= 1
            elif num < target:
                j += 1
            else:
                return True

        return False
