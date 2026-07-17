from typing import List
from bisect import bisect_right
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1
        gcd_count = [0] * (max_num + 1)
        for g in range(max_num, 0, -1):
            count = 0
            for multiple in range(g, max_num + 1, g):
                count += freq[multiple]
                gcd_count[g] -= gcd_count[multiple]
            gcd_count[g] += count * (count - 1) // 2
        prefix = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            prefix[i] = prefix[i - 1] + gcd_count[i]
        answer = []
        for q in queries:
            answer.append(bisect_right(prefix, q))
        return answer