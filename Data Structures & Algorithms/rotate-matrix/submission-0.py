class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        # transpose
        N = len(matrix)
        for i in range(N):
            for j in range(i+1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]