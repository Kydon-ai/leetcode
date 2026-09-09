from functions import timer

class Solution:
    @timer
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        line_top,line_bottom = 0,len(matrix)-1
        col_left,col_right = 0,len(matrix[0])-1

        while line_top <=line_bottom and col_left<=col_right:
            res.extend(self.get_next([line[col_left:col_right+1] for line in matrix[line_top:line_bottom+1] ]))
            # res.extend(self.get_next([matrix[line_top:line_bottom+1][0][col_left:col_right+1]]))
            line_top +=1
            line_bottom -=1
            col_left +=1
            col_right -=1
        return res
    
    def get_next(self,matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix:
            return res
        if len(matrix) ==1:
            return matrix[0]
        if len(matrix[0])==1:
            for i in matrix:
                res.append(i[0])
            return res
        for i in range(len(matrix[0])):
            if i== len(matrix[0])-1:
                break
            res.append(matrix[0][i])
        for i in range(len(matrix)):
            if i== len(matrix)-1:
                break
            res.append(matrix[i][-1])
        for i in reversed(range(len(matrix[0]))):
            if i ==0:
                break
            res.append(matrix[-1][i])
        for i in reversed(range(len(matrix))):
            if i ==0:
                break
            res.append(matrix[i][0])
        return res
        


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[3],[2]]
# print("初始：",matrix[1:2][0][1:2])
s = Solution()

print(s.spiralOrder(matrix=matrix))

