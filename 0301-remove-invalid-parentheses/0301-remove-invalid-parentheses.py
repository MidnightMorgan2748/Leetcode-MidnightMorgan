from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(t: str) -> bool:
            a = 0
            for ch in t:
                if ch == '(':
                    a += 1
                elif ch == ')':
                    a -= 1
                    if a < 0:
                        return False
            return a == 0
        queue = deque([s])
        b = {s}
        c = []
        found = False
        
        while queue:
            curr = queue.popleft()
            if is_valid(curr):
                c.append(curr)
                found = True
            if found:
                continue
            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue
                nxt = curr[:i] + curr[i+1:]
                if nxt not in b:
                    b.add(nxt)
                    queue.append(nxt)
        return c