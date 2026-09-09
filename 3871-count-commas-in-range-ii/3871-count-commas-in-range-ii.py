class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        length = len(str(n))
        
        for i in range(4, length + 1):
            start = 10**(i - 1)
            end = min(n, 10**i - 1)
            num_commas = (i - 1) // 3
            total_commas += (end - start + 1) * num_commas
            
        return total_commas