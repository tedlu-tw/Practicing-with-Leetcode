class Solution:
    def solve(self, B, C) -> bool:
        def values(B, x, y):
            s = { '1', '2', '3', '4', '5', '6', '7', '8', '9' }
            sx = (x // 3) * 3
            sy = (y // 3) * 3
            for i in range(9):
                s.discard(B[y][i])
                s.discard(B[i][x])
                s.discard(B[sy + i // 3][sx + i % 3])
            return s
        if len(C) == 0:
            return True
        x, y = C[0]
        nC = C[1:]
        for v in values(B, x, y):
            B[y][x] = v
            if self.solve(B, nC):
                return True
        B[y][x] = '.'
        return False
    def solveSudoku(self, board: List[List[str]]) -> None:
        C = [(x, y) for y in range(9) for x in range(9) if board[y][x] == '.']
        self.solve(board, C)
        
