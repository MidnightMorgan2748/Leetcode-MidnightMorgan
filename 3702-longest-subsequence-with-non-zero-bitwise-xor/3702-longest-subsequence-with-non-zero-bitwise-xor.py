class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        
        xor_all = 0
        for num in nums:
            xor_all ^= num
            
        if xor_all != 0:
            return n
        
        if all(num == 0 for num in nums):
            return 0
            
        return n - 1