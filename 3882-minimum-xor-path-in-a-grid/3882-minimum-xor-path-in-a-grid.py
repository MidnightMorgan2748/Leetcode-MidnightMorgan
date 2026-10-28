class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[None] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    dp[i][j] = {v}
                    continue
                s = set()
                if i > 0:
                    s |= dp[i - 1][j]
                if j > 0:
                    s |= dp[i][j - 1]
                dp[i][j] = {x ^ v for x in s}
        return min(dp[m - 1][n - 1])