import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            a = 1
            b = 0
            c = 1
            for j in range(i, n):
                a *= nums[j]
                b = math.gcd(b, nums[j])
                c = math.lcm(c, nums[j])
                if a == b * c:
                    max_len = max(max_len, j - i + 1)
                elif a > b * c:
                    break
                    
        return max_len