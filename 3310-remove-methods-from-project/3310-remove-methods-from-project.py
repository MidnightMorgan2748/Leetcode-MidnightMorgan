from collections import defaultdict, deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for u, v in invocations:
            adj[u].append(v)
            
        suspicious = set()
        queue = deque([k])
        suspicious.add(k)
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        can_remove = True
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                can_remove = False
                break
        if can_path_remove := can_remove:
            return [i for i in range(n) if i not in suspicious]
        else:
            return list(range(n))