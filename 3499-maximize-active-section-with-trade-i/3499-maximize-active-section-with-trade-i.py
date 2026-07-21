class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = 0
        prev_zero_block = float("-inf")
        max_merge = 0
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            length = j - i
            if s[i] == '1':
                ones += length
            else:
                max_merge = max(max_merge, prev_zero_block + length)
                prev_zero_block = length
            i = j
        return ones + max_merge
