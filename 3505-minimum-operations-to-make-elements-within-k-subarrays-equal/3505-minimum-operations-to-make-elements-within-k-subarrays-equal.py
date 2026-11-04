class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        idx = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        cb = [0] * (m + 1)
        sb = [0] * (m + 1)
        LOG = 1
        while (1 << LOG) <= m:
            LOG += 1

        def update(p, c, s):
            while p <= m:
                cb[p] += c
                sb[p] += s
                p += p & -p

        r = (x + 1) // 2
        total = 0
        cost = [0] * (n - x + 1)
        for i in range(n):
            update(idx[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(idx[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                pos = 0
                rem = r
                cnt = 0
                sm = 0
                for b in range(LOG - 1, -1, -1):
                    np_ = pos + (1 << b)
                    if np_ <= m and cb[np_] < rem:
                        pos = np_
                        rem -= cb[np_]
                        cnt += cb[np_]
                        sm += sb[np_]
                v = vals[pos]
                low = sm + v * (r - cnt)
                cost[i - x + 1] = v * r - low + (total - low) - v * (x - r)

        INF = float('inf')
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                best = cur[i - 1]
                if i >= x:
                    c = prev[i - x] + cost[i - x]
                    if c < best:
                        best = c
                cur[i] = best
            prev = cur
        return prev[n]