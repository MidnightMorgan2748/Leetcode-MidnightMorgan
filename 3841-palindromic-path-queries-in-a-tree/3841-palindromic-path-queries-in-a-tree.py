class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        base = [0] * n
        chars = [ord(c) - 97 for c in s]
        timer = 0
        stack = [(0, 0, 0)]
        base[0] = 1 << chars[0]
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                tin[u] = timer
                timer += 1
                stack.append((u, p, 1))
                for w in adj[u]:
                    if w != p:
                        up[0][w] = u
                        depth[w] = depth[u] + 1
                        base[w] = base[u] ^ (1 << chars[w])
                        stack.append((w, u, 0))
            else:
                tout[u] = timer
        for k in range(1, LOG):
            prev = up[k - 1]
            cur = up[k]
            for v in range(n):
                cur[v] = prev[prev[v]]
        bit = [0] * (n + 2)

        def add(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def get(i):
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            k = 0
            while diff:
                if diff & 1:
                    a = up[k][a]
                diff >>= 1
                k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return up[0][a]

        res = []
        for q in queries:
            t, a, b = q.split()
            if t == "update":
                x = int(a)
                c = ord(b) - 97
                if c != chars[x]:
                    d = (1 << chars[x]) ^ (1 << c)
                    chars[x] = c
                    add(tin[x], d)
                    add(tout[x], d)
            else:
                u, v = int(a), int(b)
                l = lca(u, v)
                mask = base[u] ^ get(tin[u]) ^ base[v] ^ get(tin[v]) ^ (1 << chars[l])
                res.append(mask & (mask - 1) == 0)
        return res