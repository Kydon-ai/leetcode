class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        N = len(nums)
        for i in range(N):
            while (nums[i] >=1  and nums[i] != i+1 and nums[i]<=N  and nums[nums[i]-1] !=nums[i]):
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        print(nums)
        for i in range(N):
            if (nums[i] != i+1):
                return i+1
        return N+1
                

# nums = [1,2,0]
nums = [7,8,9,11,12]
nums = [1]
nums = [1,1]
nums = [0,1,2]
nums = [3,4,-1,1]
s = Solution()

print(s.firstMissingPositive(nums=nums))