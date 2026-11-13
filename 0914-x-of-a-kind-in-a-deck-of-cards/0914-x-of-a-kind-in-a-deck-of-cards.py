class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from math import gcd
        from functools import reduce
        return reduce(gcd, Counter(deck).values()) >= 2