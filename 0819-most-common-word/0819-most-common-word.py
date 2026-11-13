class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        from collections import Counter
        ban = set(banned)
        words = re.findall(r"[a-z]+", paragraph.lower())
        cnt = Counter(w for w in words if w not in ban)
        return max(cnt, key=cnt.get)