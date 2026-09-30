class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        a = arr.sort()
        res = True
        b = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != b:
                return False
        return res 