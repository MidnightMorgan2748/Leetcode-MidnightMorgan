class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda l: l[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        cnt = [0] * (n + 1)
        active = 0
        lo = 0
        hi = 0
        m = len(logs)
        res = [0] * len(queries)
        for qi in order:
            q = queries[qi]
            while hi < m and logs[hi][1] <= q:
                s = logs[hi][0]
                if cnt[s] == 0:
                    active += 1
                cnt[s] += 1
                hi += 1
            while lo < hi and logs[lo][1] < q - x:
                s = logs[lo][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    active -= 1
                lo += 1
            res[qi] = n - active
        return res