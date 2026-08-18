from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        if k == 1:
            counts = {}
            for x in nums:
                counts[x] = counts.get(x, 0) + 1
            valid = [x for x, freq in counts.items() if freq == 1]
            return max(valid) if valid else -1
            
        if k == n:
            return max(nums)
        candidates = set()
        
        freq = {}
        for i in range(n - k + 1):
            sub = nums[i:i+k]
            seen_in_sub = set(sub)
            for val in seen_in_sub:
                freq[val] = freq.get(val, 0) + 1
                
        ans = -1
        for x in [nums[0], nums[n - 1]]:
            if freq.get(x, 0) == 1:
                ans = max(ans, x)
                
        return ans
