class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if target < matrix[0][0] or matrix[-1][-1] < target:
        #     return False

        # i = bisect_left(matrix, target, key=lambda x: x[-1])

        # j = bisect_left(matrix[i], target)

        # return matrix[i][j] == target

        m = len(matrix)

        n = len(matrix[0])

        lo = 0

        hi = m * n

        while lo < hi:
            mid = (lo + hi) // 2

            val = matrix[mid // n][mid % n]

            if val < target:
                lo = mid + 1
            elif val > target:
                hi = mid
            else:
                return True

        return False
