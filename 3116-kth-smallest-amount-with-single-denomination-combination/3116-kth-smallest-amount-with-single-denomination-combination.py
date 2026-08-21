from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count(mid: int) -> int:
            total = 0
            n = len(coins)
            for mask in range(1, 1 << n):
                lcm_val = 1
                valid = True
                for i in range(n):
                    if (mask >> i) & 1:
                        g = gcd(lcm_val, coins[i])
                        lcm_val = (lcm_val * coins[i]) // g
                        if lcm_val > mid:
                            valid = False
                            break
                
                if valid:
                    bits = mask.bit_count()
                    if bits % 2 == 1:
                        total += mid // lcm_val
                    else:
                        total -= mid // lcm_val
            return total

        
        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        Id = ans
        return Id