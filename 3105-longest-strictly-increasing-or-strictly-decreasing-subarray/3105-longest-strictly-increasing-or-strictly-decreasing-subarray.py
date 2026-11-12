class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1 & nums[0] == 1:
            return 1
        res = 0
        a = []
        a.append(nums[0])
        for i in range(1, len(nums)):
            if a[-1] >= nums[i]:
                a = []
            a.append(nums[i])
            res = max(res, len(a))
        res2 = 0
        b = []
        b.append(nums[0])
        for i in range(1, len(nums)):
            if b[-1] <= nums[i]:
                b = []
            b.append(nums[i])
            res2 = max(res2, len(b))

        return max(res, res2)
