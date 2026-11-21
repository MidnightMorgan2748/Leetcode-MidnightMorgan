class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        newp = parent[:]
        last = [-1] * 26
        order = []
        stack = [(0, 0)]
        saved = {}
        while stack:
            u, state = stack.pop()
            c = ord(s[u]) - 97
            if state == 0:
                order.append(u)
                if last[c] != -1:
                    newp[u] = last[c]
                saved[u] = last[c]
                last[c] = u
                stack.append((u, 1))
                for v in children[u]:
                    stack.append((v, 0))
            else:
                last[c] = saved[u]
        size = [1] * n
        for u in reversed(order):
            if u != 0:
                size[newp[u]] += size[u]
        return size