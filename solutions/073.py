class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        line,col = len(matrix),len(matrix[0])
        line_lists = [False for _ in range(line)]
        col_lists = [False for _ in range(col)]
        
        for i in range(line):
            for j in range(col):
                if matrix[i][j] == 0:
                    line_lists[i] = True
                    col_lists[j] = True
        for i in range(line):
            if line_lists[i]:
                for j in range(col):
                    matrix[i][j] = 0
        for i in range(col):
            if col_lists[i]:
                for j in range(line):
                    matrix[j][i] = 0
        # print(matrix)
        # matrix[:] = matrix
        


matrix = [[1,1,1],[1,0,1],[1,1,1]]
s = Solution()
s.setZeroes(matrix=matrix)
print(matrix)