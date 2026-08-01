class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def max_diff(left, right):
            if left == right:
                return nums[left]
            if (left, right) in memo:
                return memo[(left, right)]
            pick_left = nums[left] - max_diff(left + 1, right)
            pick_right = nums[right] - max_diff(left, right - 1)
            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]
        return max_diff(0, len(nums) - 1) >= 0