class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ATLvisited = set()
        PACvisited = set() 
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []
        qATL = collections.deque()
        qPAC = collections.deque()

        for r in range(ROWS):
            ATLvisited.add((r, COLS - 1))
            PACvisited.add((r, 0))
            qATL.append((r, COLS - 1))
            qPAC.append((r, 0))

        for c in range(COLS):
            ATLvisited.add((ROWS - 1, c))
            PACvisited.add((0, c))
            qATL.append((ROWS - 1, c))
            qPAC.append((0, c))
        
        def bfsATL():
            while qATL: 
                cr, cc = qATL.popleft()
                DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in DIRECTIONS:
                    nr, nc = dr + cr, dc + cc
                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        (nr, nc) not in ATLvisited):
                        if (heights[nr][nc] >= heights[cr][cc]):
                            qATL.append((nr, nc))
                            ATLvisited.add((nr, nc))
        
        def bfsPAC():
            while qPAC: 
                cr, cc = qPAC.popleft()
                DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in DIRECTIONS:
                    nr, nc = dr + cr, dc + cc
                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        (nr, nc) not in PACvisited):
                        if (heights[nr][nc] >= heights[cr][cc]):
                            qPAC.append((nr, nc))
                            PACvisited.add((nr, nc))
        
        bfsATL()
        bfsPAC()

        for r in range(ROWS):
            for c in range(COLS): 
                if (r, c) in PACvisited and (r, c) in ATLvisited: 
                    res.append((r, c))
        return res

