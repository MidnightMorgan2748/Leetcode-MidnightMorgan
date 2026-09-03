class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odds = [x for x in nums1 if x % 2 != 0]
        evens = [x for x in nums1 if x % 2 == 0]
        
        if not odds:
            return True
            
        min_odd = min(odds)
        
        if not evens:
            return True
            
        min_even = min(evens)
        
        return min_odd < min_even