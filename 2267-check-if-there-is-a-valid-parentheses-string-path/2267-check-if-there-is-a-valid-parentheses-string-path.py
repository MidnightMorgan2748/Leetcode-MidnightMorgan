class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 or grid[0][0] == ')' or  grid[m-1][n-1] == '(':
            return False
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 << 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                prev = 0
                if i >  0:
                    prev |= dp[i-1][j]
                if j > 0:
                    prev |= dp[i][j-1]
                if grid[i][j] == '(':
                    dp[i][j] =  prev << 1
                else:
                    dp[i][j] = prev >> 1
        return dp[m-1][n-1] & 1 == 1