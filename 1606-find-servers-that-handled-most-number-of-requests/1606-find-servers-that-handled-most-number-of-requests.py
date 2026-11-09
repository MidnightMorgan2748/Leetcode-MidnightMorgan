class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        import heapq
        free = list(range(k))
        heapq.heapify(free)
        busy = []
        cnt = [0] * k
        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, s = heapq.heappop(busy)
                heapq.heappush(free, i + ((s - i) % k))
            if not free:
                continue
            s = heapq.heappop(free) % k
            cnt[s] += 1
            heapq.heappush(busy, (a + l, s))
        mx = max(cnt)
        return [i for i in range(k) if cnt[i] == mx]