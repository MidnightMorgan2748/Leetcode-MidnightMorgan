from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        counts = Counter(tuple(sorted(d)) for d in dominoes)
        
        res = 0
        for a in counts.values():
            res += a * (a - 1) // 2
            
        return res