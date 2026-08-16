class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        num_reqs = len(requests)
        if num_reqs == 0:
            return 0

        INF = float('inf')
        full_mask = (1 << num_reqs) - 1

        dp = [[INF] * num_reqs for _ in range(1 << num_reqs)]

        for i in range(num_reqs):
            arr, fl = requests[i]
            dp[1 << i][i] = max(abs(start - fl), arr)

        for mask in range(1, full_mask + 1):
            for last in range(num_reqs):
                cur_time = dp[mask][last]
                if cur_time == INF:
                    continue
                if not (mask & (1 << last)):
                    continue
                _, last_fl = requests[last]
                for nxt in range(num_reqs):
                    if mask & (1 << nxt):
                        continue
                    arr, fl = requests[nxt]
                    new_time = max(cur_time + abs(last_fl - fl), arr)
                    nmask = mask | (1 << nxt)
                    if new_time < dp[nmask][nxt]:
                        dp[nmask][nxt] = new_time

        return min(dp[full_mask][last] for last in range(num_reqs))