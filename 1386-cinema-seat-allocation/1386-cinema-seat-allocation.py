class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        import collections
        
        row_reserved = collections.defaultdict(int)
        for r, s in reservedSeats:
            if 2 <= s <= 9:
                row_reserved[r] |= (1 << (s - 2))
                
        ans = (n - len(row_reserved)) * 2
        
        left = 0b00001111     # seats 2, 3, 4, 5
        middle = 0b00111100   # seats 4, 5, 6, 7
        right = 0b11110000    # seats 6, 7, 8, 9
        
        for r, mask in row_reserved.items():
            allocated = False
            if (mask & left) == 0:
                ans += 1
                allocated = True
            if (mask & right) == 0:
                ans += 1
                allocated = True
            if not allocated and (mask & middle) == 0:
                ans += 1
                
        return ans