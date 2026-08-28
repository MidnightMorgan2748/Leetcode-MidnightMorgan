class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-97] += 1
        odd = [i for i in range(26) if freq[i] % 2]
        if n % 2 == 0:
            if odd:
                return ""
            mid = ""
        else:
            if len(odd) != 1:
                return ""
            mid = chr(odd[0]+97)
        half_len = n // 2
        counts = [freq[i]//2 for i in range(26)]
        t_half = target[:half_len]

        def build(half):
            return half + mid + half[::-1] if n % 2 else half + half[::-1]

        result = [None]*half_len
        stack = []
        matched = True
        for i in range(half_len):
            tidx = ord(t_half[i]) - 97
            gidx = None
            for c in range(tidx+1, 26):
                if counts[c] > 0:
                    gidx = c
                    break
            if gidx is not None:
                snap = counts[:]
                snap[gidx] -= 1
                stack.append((i, chr(gidx+97), snap))
            if counts[tidx] > 0:
                result[i] = t_half[i]
                counts[tidx] -= 1
            else:
                matched = False
                break

        if matched:
            cand = build(t_half)
            if cand > target:
                return cand

        if not stack:
            return ""

        pos, ch, snap = stack.pop()
        result[pos] = ch
        counts = snap
        remaining = []
        for c in range(26):
            remaining.extend([chr(c+97)]*counts[c])
        half = ''.join(result[:pos+1]) + ''.join(remaining)
        return build(half)