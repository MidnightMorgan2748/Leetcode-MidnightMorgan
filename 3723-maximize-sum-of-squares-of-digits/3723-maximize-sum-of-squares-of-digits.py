class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        a, b = divmod(sum, 9)
        res = "9" * a
        if b:
            res += str(b)
        return res + "0" * (num - len(res))