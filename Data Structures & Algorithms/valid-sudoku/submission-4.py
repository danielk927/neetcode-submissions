class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validRow(): 
            for rowidx in range(len(board)):
                row = board[rowidx]
                seen = set()
                for i in range(len(row)):
                    if row[i] == ".":
                        continue
                    if row[i] in seen: 
                        return False
                    seen.add(row[i])
            return True

        def validCol():
            for colidx in range(len(board[0])):
                seen = set()
                for rowidx in range(len(board)):
                    val = board[rowidx][colidx]
                    if val == ".":
                        continue
                    if val in seen: 
                        return False
                    seen.add(val)
            return True


        def validBox(): 
            for boxRow in range(3):
                for boxCol in range(3): 
                    startRow = boxRow * 3
                    startCol = boxCol * 3
                    seen = set() 
                    for r in range(3): 
                        for c in range(3):
                            val = board[startRow + r][startCol + c]
                            if val == ".":
                                continue
                            if val in seen: 
                                return False
                            seen.add(val)
            return True

        if validRow() and validCol() and validBox():
            return True
        else:
            return False