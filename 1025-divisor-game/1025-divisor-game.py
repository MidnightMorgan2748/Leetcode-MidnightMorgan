class Solution:
    def divisorGame(self, n: int) -> bool:
        res = 0
        while n!= 1:
            n -= 1
            res += 1
        return res % 2 == 1