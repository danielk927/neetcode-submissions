class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                cr, cc = q.popleft()          
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc  
                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands