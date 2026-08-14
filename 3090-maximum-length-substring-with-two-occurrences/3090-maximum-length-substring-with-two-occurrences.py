class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import defaultdict
        
        char_count = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char_count[s[right]] += 1
            
            while char_count[s[right]] > 2:
                char_count[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len