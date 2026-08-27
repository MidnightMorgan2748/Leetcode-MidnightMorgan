from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
        
        prefix = []
        for i in range(n):
            c = target[i]
            if count[c] > 0:
                count[c] -= 1
                prefix.append(c)
            else:
                break
                
        def solve(idx, current_count, current_prefix):
            if idx == n:
                return "".join(current_prefix)
                
            c = target[idx]
            if current_count[c] > 0:
                current_count[c] -= 1
                current_prefix.append(c)
                res = solve(idx + 1, current_count, current_prefix)
                if res != "":
                    return res
                current_prefix.pop()
                current_count[c] += 1
                
            for ch_code in range(ord(target[idx]) + 1, ord('z') + 1):
                ch = chr(ch_code)
                if current_count[ch] > 0:
                    current_count[ch] -= 1
                    current_prefix.append(ch)
                    remaining = []
                    for k in sorted(current_count.keys()):
                        remaining.extend([k] * current_count[k])
                    return "".join(current_prefix + remaining)
                    
            return ""

        for i in range(len(prefix), -1, -1):
            curr_count = Counter(s)
            curr_prefix = []
            possible = True
            for j in range(i):
                c = target[j]
                if curr_count[c] > 0:
                    curr_count[c] -= 1
                    curr_prefix.append(c)
                else:
                    possible = False
                    break
            if not possible:
                continue
                
            if i < n:
                found_greater = False
                for ch_code in range(ord(target[i]) + 1, ord('z') + 1):
                    ch = chr(ch_code)
                    if curr_count[ch] > 0:
                        curr_count[ch] -= 1
                        curr_prefix.append(ch)
                        found_greater = True
                        break
                if found_greater:
                    remaining = []
                    for k in sorted(curr_count.keys()):
                        remaining.extend([k] * curr_count[k])
                    candidate = "".join(curr_prefix + remaining)
                    if candidate > target:
                        return candidate
                    # Backtrack the greater character if it failed the strict greater check
                    curr_prefix.pop()
                    curr_count[ch] += 1
                
            res = solve(i, curr_count, curr_prefix)
            if res != "" and res > target:
                return res
                
        return ""
