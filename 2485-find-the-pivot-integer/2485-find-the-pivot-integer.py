class Solution:
    def pivotInteger(self, n: int) -> int:
        b = (n * (n+1))//2
        a =  0

        for x in range(1, n+1):
            a += x
            if a == b - a + x:
                return x
        return -1