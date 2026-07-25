class Solution:
    def maxProduct(self, n: int) -> int:
        a = str(n)
        num = []
        for i in a:
            num.append(int(i)) 
        res = 0
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                res = max(res, num[i] * num[j])
        return res
