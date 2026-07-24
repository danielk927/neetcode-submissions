class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0 
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set() 
        islands = 0 

        def bfs(r, c): 
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q: 
                cr, cc = q.popleft() 
                DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in DIRECTIONS: 
                    nr, nc = dr + cr, dc + cc
                    if (0 <= nr < ROWS and 0 <= nc < COLS) and grid[nr][nc] == "1" and (nr, nc) not in visited: 
                        visited.add((nr, nc)) 
                        q.append((nr, nc))
                        
        
        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited: 
                    bfs(r, c)
                    islands += 1 
        return islands