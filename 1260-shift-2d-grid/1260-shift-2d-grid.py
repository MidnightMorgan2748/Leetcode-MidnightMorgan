class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total_elements = m * n
        k = k % total_elements
        new_grid = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_idx = (i * n + j + k) % total_elements
                new_i = new_idx // n
                new_j = new_idx % n
                new_grid[new_i][new_j] = grid[i][j]
        return new_grid