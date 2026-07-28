from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        
        first_half = []
        mid_char = ""
        
        for char in sorted(count.keys()):
            freq = count[char]
            first_half.append(char * (freq // 2))
            if freq % 2 == 1:
                mid_char = char
        left = "".join(first_half)
        right = left[::-1]
        
        return left + mid_char + right