class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        if n == 0:
            return []
        result = [0 for i in range(m*n)]
        up = True
        row = col = 0
        for i in range(m*n):
            result[i] = matrix[row][col]
            if up:
                if col == n - 1:
                    row = row + 1
                    up = not up
                elif row == 0:
                    col = col + 1
                    up = not up
                else:
                    row = row - 1
                    col = col + 1
            else:
                if row == m - 1:
                    col = col + 1
                    up = not up
                elif col == 0:
                    row = row + 1
                    up = not up
                else:
                    row = row + 1
                    col = col - 1

        return result
