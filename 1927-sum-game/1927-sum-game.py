class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum1, q1 = 0, 0
        sum2, q2 = 0, 0
        
        for i in range(half):
            if num[i] == '?':
                q1 += 1
            else:
                sum1 += int(num[i])
                
        for i in range(half, n):
            if num[i] == '?':
                q2 += 1
            else:
                sum2 += int(num[i])
                
        if (q1 + q2) % 2 == 0:
            if 2 * (sum1 - sum2) == 9 * (q2 - q1):
                return False
                
        return True