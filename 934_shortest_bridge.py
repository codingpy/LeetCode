from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        q = deque()

        def dfs(i: int, j: int) -> None:
            q.append((i, j))

            grid[i][j] = 2

            for i, j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                    dfs(i, j)

        def bfs() -> int:
            k = 0

            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()

                    for i, j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= i < n and 0 <= j < n:
                            if grid[i][j] == 1:
                                return k

                            if grid[i][j] == 0:
                                q.append((i, j))

                                grid[i][j] = 3

                k += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)

                    return bfs()
