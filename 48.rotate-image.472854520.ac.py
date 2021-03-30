class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(N // 2):
            for j in range(N):
                matrix[j][i], matrix[j][N-i-1] = matrix[j][N-i-1], matrix[j][i]
        return matrix
            
