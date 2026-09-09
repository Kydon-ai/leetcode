class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current,left,right = 0,0,len(nums)-1
        while current<=right:
            if nums[current]<1:
                nums[current],nums[left] = nums[left],nums[current]
                current +=1
                left +=1
            elif nums[current] ==1:
                current +=1
            else:
                nums[current],nums[right] = nums[right],nums[current]
                right -=1



s = Solution()

nums = [2,0,2,1,1,0]
s.sortColors(nums)
print(nums)