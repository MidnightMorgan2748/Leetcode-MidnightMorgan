class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        if n < 10000:
            return n - 999
        if n < 100000:
            return (n - 9999) + 9000
        if n < 1000000:
            return (n - 99999) + 99000
        