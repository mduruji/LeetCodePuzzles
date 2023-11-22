class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a = []
        b = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    a.append(i) 
                    b.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in a or j in b:
                    matrix[i][j] = 0