class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start_x ,start_y = 0,len(matrix[0])-1
        res = False
        while matrix[start_x][start_y] != target:
            if matrix[start_x][start_y] >target:
                start_y -=1
            else:
                start_x +=1
            
            if start_y <0 or start_x >=len(matrix):
                break
        else:
            res = True
        return res



s= Solution()

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]];target = 5;
# matrix = [[-5]]; target = -2;
matrix = [[-1,3]];target = 3
matrix = [[-1],[-1]];target = -2;
matrix = [[1,3,5]];target = 5;

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]];target = 15;

print(s.searchMatrix(matrix,target))