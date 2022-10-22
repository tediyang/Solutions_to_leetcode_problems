import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = copy.deepcopy(matrix)
        n = len(mat[0]) - 1

        for i in range(len(mat[0])):
            m = 0
            for j in range(len(mat[0])):
                matrix[m][n] = mat[i][j]
                m += 1

            n -= 1