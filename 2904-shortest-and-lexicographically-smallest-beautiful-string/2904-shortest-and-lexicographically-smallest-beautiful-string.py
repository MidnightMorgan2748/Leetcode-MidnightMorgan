class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if sub.count('1') == k:
                    if ans == "" or len(sub) < len(ans) or (len(sub) == len(ans) and sub < ans):
                        ans = sub      
        return ans