class Solution:
    def rob(self, nums: list[int]) -> int:
        dp:list[list[int,int]] = [[0,0] for i in range(len(nums))]
        dp[0][0],dp[0][1] = 0,nums[0]
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                dp[i][0] = max(dp[i-1][0],dp[i-1][1])
                dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[len(nums)-1][0],dp[len(nums)-1][1])


s = Solution()

nums = [1,2,3,1]
print(s.rob(nums))