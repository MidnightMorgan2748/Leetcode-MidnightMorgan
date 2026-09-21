class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res =  [0]*k
        dp = [0] *k
        for x in nums:
            rem = x % k
            new_dp = [0] * k
            for r in range(k):
                if dp[r] > 0:
                    new_dp[(r * rem) % k] += dp[r]
            new_dp[rem] += 1
            dp = new_dp
            for r in range(k):
                res[r] += dp[r]
        return res