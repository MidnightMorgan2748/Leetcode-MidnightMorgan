class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            z = set()
            for j in range(i, n):
                z.add(nums[j])
                total += len(z) ** 2
        return total