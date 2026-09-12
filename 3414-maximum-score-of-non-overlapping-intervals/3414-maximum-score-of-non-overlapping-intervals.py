from typing import List
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])
        ls = [intervals[i][0] for i in order]
        rs = [intervals[i][1] for i in order]
        ws = [intervals[i][2] for i in order]

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            l_i = ls[i - 1]
            w_i = ws[i - 1]
            idx_i = order[i - 1]
            p = bisect_left(rs, l_i, 0, i - 1)

            dp[i][0] = (0, ())
            for k in range(1, 5):
                skip = dp[i - 1][k]
                sub_score, sub_tuple = dp[p][k - 1]
                take = (sub_score + w_i, tuple(sorted(sub_tuple + (idx_i,))))

                if skip[0] > take[0]:
                    dp[i][k] = skip
                elif take[0] > skip[0]:
                    dp[i][k] = take
                else:
                    dp[i][k] = skip if skip[1] <= take[1] else take

        return list(dp[n][4][1])