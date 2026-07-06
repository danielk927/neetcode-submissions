class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0 
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0

        def bfs (r, c): 
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q: 
                cr, cc = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions: 
                    row = cr + dr
                    col = cc + dc
                    if (0 <= row < ROWS and 
                        0 <= col < COLS and 
                        grid[row][col] == "1" and 
                        (row, col) not in visited):
                        q.append((row, col))
                        visited.add((row, col))

        for r in range(ROWS): 
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1 
        return islands


        