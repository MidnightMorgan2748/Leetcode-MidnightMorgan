class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def mult(n):
            a = str(n)
            b = 1
            for i in a:
                b *= int(i)
            return b
        z = n
        a = mult(n)
        while a % t != 0:
            z += 1
            a = mult(z)
        return z