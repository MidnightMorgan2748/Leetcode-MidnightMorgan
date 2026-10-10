class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        suu = [abs(a-b) for a, b in zip(nums1, nums2)]
        if sum(suu) <= k:
            return 0
        mx =  max(suu)
        a = [0] * (mx + 1)
        for d in suu:
            a[d] += 1
        for v in range(mx, 0, -1):
            if a[v] == 0:
                continue
            if a[v] <= k:
                k -= a[v]
                a[v - 1] += a[v]
                a[v] = 0
            else:
                a[v] -= k
                a[v - 1] += k
                k = 0
                break
        return sum(i * i *  c for i, c in enumerate(a))