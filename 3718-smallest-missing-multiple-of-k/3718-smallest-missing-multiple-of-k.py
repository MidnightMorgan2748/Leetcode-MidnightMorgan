class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a = len(nums)
        for i in range(1, a+2):
            if (k * i) not in nums:
                return k*i