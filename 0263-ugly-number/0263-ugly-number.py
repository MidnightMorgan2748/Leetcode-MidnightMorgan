class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        suka = [2, 3, 5]
        for factor in suka:
            while n % factor == 0:
                n //= factor

        return n == 1