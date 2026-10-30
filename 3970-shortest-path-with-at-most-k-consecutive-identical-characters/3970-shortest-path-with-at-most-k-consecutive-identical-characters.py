class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        import heapq
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w, labels[u] == labels[v]))
        INF = float('inf')
        dist = [INF] * (n * (k + 1))
        dist[1] = 0
        pq = [(0, 0, 1)]
        while pq:
            d, u, r = heapq.heappop(pq)
            if d > dist[u * (k + 1) + r]:
                continue
            if u == n - 1:
                return d
            for v, w, same in adj[u]:
                nr = r + 1 if same else 1
                if nr > k:
                    continue
                nd = d + w
                idx = v * (k + 1) + nr
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq.heappush(pq, (nd, v, nr))
        return -1