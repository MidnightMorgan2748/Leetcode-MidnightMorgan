class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        list1 = []
        list2 = []
        
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    list1.append((r, c))
                if img2[r][c] == 1:
                    list2.append((r, c))
                    
        count = collections.defaultdict(int)
        for r1, c1 in list1:
            for r2, c2 in list2:
                count[(r2 - r1, c2 - c1)] += 1
                
        return max(count.values()) if count else 0