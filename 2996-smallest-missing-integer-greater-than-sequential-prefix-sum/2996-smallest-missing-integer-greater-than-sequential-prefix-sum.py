class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
                
        nums_set = set(nums)
        ans = prefix_sum
        while ans in nums_set:
            ans += 1
            
        return ans