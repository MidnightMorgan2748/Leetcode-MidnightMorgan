from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        suf = [0] * (n + 1)
        
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = m - 1 - j
            
        ans = []
        changed = False
        j = 0
        for i in range(n):
            if j < m and word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed and j + 1 < m and suf[i + 1] >= m - (j + 1):
                ans.append(i)
                changed = True
                j += 1
            elif not changed and j == m - 1:
                ans.append(i)
                changed = True
                j += 1
                
            if j == m:
                return ans
                
        return []
