class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = max(nums)
        b = min(nums)
        c = []
        for i in range(b, a + 1):
            if i not in set(nums):
                c.append(i)
        return c