class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        index = 0
        res = -1
        for i in nums:
            a = str(i)
            su = 0
            for j in a:
                su += int(j)
            if index == su:
                res = index
                break
            index += 1
        return res