class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10 **9 + 7
        n = len(nums)
        b1 = [0] * (n+2)
        b2 = [0] * (n+2)
        def upd(b, i, v):
            while i <= n + 1:
                b[i] += v
                i += i & -i
        def qry(b, i):
            s = 0
            while i > 0:
                s += b[i]
                i -= i & -i
            return s
        def range_add(l, r, v):
            upd(b1, l, v)
            upd(b1, r+1, -v)
            upd(b2, l, v * (l-1))
            upd(b2, r+1, -v*r)

        def prefix(i):
            return qry(b1, i) * i - qry(b2, i)
        
        last = {}
        cur = 0
        ans = 0
        for j, x in enumerate(nums):
            l = last.get(x, -1) + 1
            s = prefix(j) - prefix(l)
            length = j - l + 1
            cur += 2 * s + length
            range_add(l+1, j+1, 1)
            last[x] = j
            ans = (ans + cur) % MOD
        return ans