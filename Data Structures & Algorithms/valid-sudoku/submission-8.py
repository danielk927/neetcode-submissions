class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidRow(board): 
            for i in range(9):
                num = set() 
                for j in range(9):
                    if board[i][j] in num and board[i][j] != '.': 
                        return False
                    else:
                        num.add(board[i][j])
            return True
        
        def isValidCol(board): 
            for i in range(9): 
                num = set()
                for j in range(9): 
                    if board[j][i] in num and board[j][i] != '.':
                        return False
                    else:
                        num.add(board[j][i])
            return True

        def isValidBox(board):
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    num = set()
                    for k in range(3):
                        for l in range(3): 
                            if board[i + k][j + l] in num and board[i + k][j + l] != '.': 
                                return False
                            else:
                                num.add(board[i + k][j + l])
            return True
        
        return isValidRow(board) and isValidCol(board) and isValidBox(board)
