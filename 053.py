class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        global_max = current_max = nums[0]
        for num in nums:
            current_max = max(num,current_max + num)
            global_max = max(current_max,global_max)
        return global_max


s = Solution()

# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
# nums = [0]
# nums = [-1]
# nums = [5,4,-1,7,8]
# nums = [-1,3,1,-1]

# nums = [2,-3,1,3,-3,2,2,1]

# nums = [-2,-1]

# nums = [-1,0,-1,2,-3,1,2,3,-2]
# nums = [2,-1,2,1,3,-2,1,2,1,-2]
print(s.maxSubArray(nums))