class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        output = 0
        index = matrix[0].index(min(matrix[0]))
        temp = []
        for i in range(0, len(matrix), 1):
            if matrix[i].index(min(matrix[i])) == index or matrix[i].index(min(matrix[i])) == index + 1 or matrix[i].index(min(matrix[i])) == index - 1:
                output += min(matrix[i])
                index = matrix[i].index(min(matrix[i]))
            else:
                temp = []
                for j in range(0, len(matrix[i]), 1):
                    if j == index or j == index + 1 or j == index - 1:
                        temp.append(matrix[i][j])
                output += min(temp)
        return output
