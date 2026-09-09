class Solution:
    def maxArea(self, height: list[int]) -> int:
        i_left,i_right = 0,len(height)-1
        sum_max = 0
        while(i_left <=i_right):
            temp_res= min(height[i_left],height[i_right]) * (i_right - i_left)
            if (temp_res > sum_max):
                sum_max = temp_res
        
            if height[i_left] <=height[i_right]:
                i_left = i_left + 1  
            else:
                i_right = i_right - 1
        return sum_max



s = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(height))