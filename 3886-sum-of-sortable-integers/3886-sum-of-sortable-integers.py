class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        x = [0] * n
        for i in range(1, n):
            x[i] = x[i-1] + (1 if nums[i-1] > nums[i] else 0)
        c = 0
        for k in range(1, n+1):
            if n % k:
                continue
            z = True
            v = 0
            for s in range(0, n, k):
                e = s + k - 1
                desc = x[e] - x[s] + (1 if nums[e] > nums[s] else 0)
                block = nums[s: e+1]
                if desc > 1 or min(block) < v:
                    z = False
                    break
                v = max(block)
            if z:
                c += k
        return c