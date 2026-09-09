class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        nums = []
        for a_list in matrix:
            nums.extend(a_list)
        
        i_left ,i_right = 0,len(nums)-1
        FLAG = False
        while i_left <= i_right:
            mid = int((i_left + i_right) /2)
            if nums[mid] == target:
                FLAG = True
                break
            if target >= nums[mid]:
                i_left = mid+1
            else:
                i_right = mid
        
        return FLAG


s= Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 3;
matrix =[[1,3,5,7],[10,11,16,20],[23,30,34,60]];target = 13;
print(s.searchMatrix(matrix,target))