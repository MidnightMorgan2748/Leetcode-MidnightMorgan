class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter

        n = len(s)
        half_n = n // 2
        count = Counter(s)

        chars = sorted(count.keys())
        half_count = {ch: count[ch] // 2 for ch in chars}
        
        center_char = ""
        for ch in chars:
            if count[ch] % 2 == 1:
                center_char = ch
                break

        def count_permutations(rem_total, counts_dict):
            items = []
            for ch in sorted(counts_dict.keys()):
                for _ in range(counts_dict[ch]):
                    items.append(ch)
            
            y = 1
            cur_n = rem_total
            
            from math import comb
            rem = rem_total
            for ch in chars:
                c = counts_dict[ch]
                if c > 0:
                    y *= comb(rem, c)
                    if y > k:
                        return y
                    rem -= c
            return y

        first_half = []
        rem_total = half_n

        for _ in range(half_n):
            found = False
            for ch in chars:
                if half_count[ch] == 0:
                    continue
                
                half_count[ch] -= 1
                rem_total -= 1
                
                ways = count_permutations(rem_total, half_count)
                
                if ways >= k:
                    first_half.append(ch)
                    found = True
                    break
                else:
                    k -= ways
                    half_count[ch] += 1
                    rem_total += 1
            
            if not found:
                return ""

        half_str = "".join(first_half)
        return half_str + center_char + half_str[::-1]
