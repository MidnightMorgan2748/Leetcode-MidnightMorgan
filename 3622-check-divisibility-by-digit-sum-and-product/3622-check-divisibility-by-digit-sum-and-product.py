class Solution:
    def checkDivisibility(self, n: int) -> bool:
        char_sum = 0
        char_mul = 1
        for i in str(n):
            char_sum += int(i)
            char_mul *= int(i)
        return n % (char_sum + char_mul) == 0
