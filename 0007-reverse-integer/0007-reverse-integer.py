class Solution:
    def reverse(self, x: int) -> int:
        a, b = -2**31, 2**31 - 1
        c = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x != 0:
            digit = x % 10
            x //= 10
            if res > (b - digit) // 10:
                return 0
            res = res * 10 + digit
        return c * res