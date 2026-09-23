class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        mi = sum(nums) - x
        if mi < 0:
            return -1
        if mi == 0:
            return len(nums)
        n = len(nums)
        max_len = -1
        bo = 0
        left = 0
        for right in range(n):
            bo += nums[right]
            while bo > mi and left <= right:
                bo -= nums[left]
                left += 1
            if bo == mi:
                max_len = max(max_len, right - left + 1)
        return n - max_len if max_len != -1 else -1