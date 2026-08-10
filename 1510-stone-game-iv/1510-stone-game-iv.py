class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            root = 1
            while root * root <= i:
                if not dp[i - root * root]:
                    dp[i] = True
                    break
                root += 1
        return dp[n]