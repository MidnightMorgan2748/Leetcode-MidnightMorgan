class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        a = []
        b = 0
        for c in seq:
            if c == '(':
                b += 1
                a.append(b % 2)
            else:
                a.append(b % 2)
                b -= 1
        return a