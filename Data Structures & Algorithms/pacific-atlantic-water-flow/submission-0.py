class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []

        def canReachPac(r, c):
            visited = set() 
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q: 
                DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                cr, cc = q.popleft()
                if (cr == 0 or cc == 0):
                    return True
                for dr, dc in DIRECTIONS: 
                    nr, nc = cr + dr, cc + dc 
                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        (nr, nc) not in visited):
                        if (heights[nr][nc] <= heights[cr][cc]):
                                q.append((nr, nc))
                                visited.add((nr, nc))
            return False

        
        def canReachAtl(r, c):
            visited = set() 
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q: 
                DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                cr, cc = q.popleft()
                if (cr == ROWS - 1 or cc == COLS - 1):
                    return True
                for dr, dc in DIRECTIONS: 
                    nr, nc = cr + dr, cc + dc 
                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        (nr, nc) not in visited):
                        if (heights[nr][nc] <= heights[cr][cc]):
                                q.append((nr, nc))
                                visited.add((nr, nc))
            return False

        for r in range(ROWS): 
            for c in range(COLS): 
                if canReachPac(r, c) == True and canReachAtl(r, c) == True: 
                    res.append((r, c))
        return res