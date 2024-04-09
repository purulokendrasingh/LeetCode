class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_ends, col_ends = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_ends.add(i)
                    col_ends.add(j)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    if i in row_ends or j in col_ends:
                        matrix[i][j] = 0
                