class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        for a in (0, 1):
            arr = nums[::-1] if a else nums
            pos = [0] *  n
            for i, x in enumerate(arr):
                pos[x] = i
            for c in (0, 1):
                first = n-1 if c else 0
                step = -1 if c else 1
                b = pos[first]
                if all(arr[(b+i) %  n] == first + step * i for i in range(n)):
                    ans = min(ans, a+b+c)
        return -1 if ans == float('inf') else ans