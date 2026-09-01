from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        from collections import deque
        
        m = len(classroom)
        n = len(classroom[0])
        
        litter_positions = []
        start_x, start_y = -1, -1
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_x, start_y = r, c
                elif classroom[r][c] == 'L':
                    litter_positions.append((r, c))
                    
        num_litter = len(litter_positions)
        litter_map = {pos: i for i, pos in enumerate(litter_positions)}
        
        full_mask = (1 << num_litter) - 1
        
        queue = deque([(start_x, start_y, 0, energy, 0)])
        best_energy = {}
        best_energy[(start_x, start_y, 0)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y, mask, e, steps = queue.popleft()
            
            if mask == full_mask:
                return steps
                
            if e <= 0:
                continue
                
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    ne = e - 1
                    if ne < 0:
                        continue
                        
                    nmask = mask
                    if classroom[nx][ny] == 'L':
                        idx = litter_map[(nx, ny)]
                        nmask |= (1 << idx)
                        
                    if nmask == full_mask:
                        return steps + 1
                        
                    curr_energy = energy if classroom[nx][ny] == 'R' else ne
                    
                    state_key = (nx, ny, nmask)
                    if state_key not in best_energy or curr_energy > best_energy[state_key]:
                        best_energy[state_key] = curr_energy
                        queue.append((nx, ny, nmask, curr_energy, steps + 1))
                        
        return -1
