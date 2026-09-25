from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            groups = []
            cur = []
            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    sub, i = parse(i+1)
                    cur.append(sub)
                elif expression[i] == ',':
                    groups.append(cur)
                    cur = []
                    i += 1
                else:
                    cur.append({expression[i]})
                    i += 1
            groups.append(cur)
            i += 1

            result = set()
            for group in groups:
                prod = {''}
                for s in group:
                    prod = {a + b for a in prod for b in s}
                result |= prod
            return result, i
        result, _ = parse(0)
        return sorted(result)