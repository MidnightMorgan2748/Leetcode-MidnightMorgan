class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        import heapq
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        res = []
        t = 0
        for j, d in enumerate(tasks):
            t = max(t, j)
            if not free and busy[0][0] > t:
                t = busy[0][0]
            while busy and busy[0][0] <= t:
                ft, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            w, i = heapq.heappop(free)
            res.append(i)
            heapq.heappush(busy, (t + d, w, i))
        return res