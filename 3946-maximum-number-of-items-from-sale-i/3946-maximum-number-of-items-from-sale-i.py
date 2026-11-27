class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        f = [0] * (budget + 1)
        mn = min(p for _, p in items)
        for factor, price in items:
            cnt = 0
            for fj, _ in items:
                if fj % factor == 0:
                    cnt += 1
            for b in range(budget, price - 1, -1):
                v = f[b - price] + cnt
                if v > f[b]:
                    f[b] = v
        return max(f[i] + (budget - i) // mn for i in range(budget + 1))