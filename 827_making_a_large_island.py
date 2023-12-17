class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ans = 0

        n = len(grid)

        k = 2

        def dfs(i: int, j: int) -> int:
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = k

                return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

            return 0

        dic = {}

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)

                    ans = max(ans, area)

                    dic[k] = area

                    k += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    islands = set()

                    for i, j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= i < n and 0 <= j < n:
                            k = grid[i][j]

                            if k:
                                islands.add(k)

                    ans = max(ans, sum([dic[k] for k in islands]) + 1)

        return ans
