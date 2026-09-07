class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            total = sum(dp) % MOD
            dp[idx] = (total + 1) % MOD
            
        return sum(dp) % MOD