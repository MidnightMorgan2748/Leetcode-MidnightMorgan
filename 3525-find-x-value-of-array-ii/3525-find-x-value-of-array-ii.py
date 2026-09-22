class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        a = [None] * (4 * n)
        def combine(a, b):
            pa, ca = a
            pb, cb = b
            cnt = ca[:]
            for r in range(k):
                cnt[pa * r % k] += cb[r]
            return pa * pb % k, cnt
        def build(b, l , r):
            if l == r:
                v = nums[l] % k
                cnt = [0] * k
                cnt[v] = 1
                a[b] = (v, cnt)
                return
            mid = (l+r) // 2
            build(2 * b, l, mid)
            build(2 * b + 1, mid + 1, r)
            a[b] = combine(a[2 * b], a[2 * b + 1])
        def update(b, l, r, i, v):
            if l == r:
                v %= k
                cnt = [0] * k
                cnt[v] = 1
                a[b] = (v, cnt)
                return
            mid = (l +  r) // 2
            update(2 * b if i <= mid else 2 * b + 1, l if i <= mid else mid + 1, mid if i <= mid else r, i, v)
            a[b] = combine(a[2 * b], a[2 * b + 1])
        def query(b, l, r, ql, qr):
            if ql <= l and r <= qr:
                return a[b]
            mid = (l + r) // 2
            if qr <= mid:
                return query(2 * b, l, mid, ql, qr)
            if ql > mid:
                return query(2 * b + 1, mid + 1, r, ql, qr)
            return combine(query(2 * b, l, mid, ql, qr), query(2 * b + 1, mid + 1, r, ql, qr))
        build(1, 0, n-1)
        ans = []
        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)
            ans.append(query(1, 0, n - 1, start, n - 1)[1][x])
        return ans