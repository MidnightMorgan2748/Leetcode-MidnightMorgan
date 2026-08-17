from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[i][j] = maximum score obtainable from stoneValue[i:j+1]
        dp = [[0] * n for _ in range(n)]

        # left_best[i][j]:
        # max(dp[i][k] + prefix[k+1]) for i <= k <= j
        left_best = [[float('-inf')] * n for _ in range(n)]

        # right_best[j][i]:
        # max(dp[k][j] - prefix[k]) for i <= k <= j
        right_best = [[float('-inf')] * n for _ in range(n)]

        # Base cases: one stone
        for i in range(n):
            left_best[i][i] = prefix[i + 1]
            right_best[i][i] = -prefix[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # We need:
                #
                # left_sum <= right_sum
                #
                # prefix[k+1] - prefix[i]
                # <=
                # prefix[j+1] - prefix[k+1]
                #
                # Therefore:
                # prefix[k+1] <= (prefix[i] + prefix[j+1]) / 2

                total_boundary = prefix[i] + prefix[j + 1]

                # Largest q such that:
                # prefix[q] <= floor(total_boundary / 2)
                q = bisect_right(
                    prefix,
                    total_boundary // 2,
                    i + 1,
                    j + 1
                ) - 1

                best = 0

                # Left side is smaller/equal.
                #
                # score =
                # left_sum + dp[i][k]
                #
                # = prefix[k+1] - prefix[i] + dp[i][k]
                #
                # = (dp[i][k] + prefix[k+1]) - prefix[i]
                #
                # left_best gives us the maximum directly.

                if q >= i + 1:
                    best = max(
                        best,
                        left_best[i][q - 1] - prefix[i]
                    )

                # Right side is smaller/equal.
                #
                # Need:
                # prefix[k+1] >= ceil(total_boundary / 2)
                #
                # Find the first such prefix index.

                q = bisect_left(
                    prefix,
                    (total_boundary + 1) // 2,
                    i + 1,
                    j + 1
                )

                if q <= j:
                    # right_sum + dp[k+1][j]
                    #
                    # = prefix[j+1] - prefix[k+1]
                    #   + dp[k+1][j]
                    #
                    # = prefix[j+1]
                    #   + (dp[k+1][j] - prefix[k+1])

                    best = max(
                        best,
                        prefix[j + 1] + right_best[j][q]
                    )

                dp[i][j] = best

                # Update structures for future intervals.

                left_best[i][j] = max(
                    left_best[i][j - 1],
                    dp[i][j] + prefix[j + 1]
                )

                right_best[j][i] = max(
                    right_best[j][i + 1],
                    dp[i][j] - prefix[i]
                )

        return dp[0][n - 1]
