class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_mult:list[int] = []
        surfix_mult:list[int] = []
        for i in range(len(nums)):
            if i==0:
                prefix_mult.append(nums[i])
            else:
                prefix_mult.append(prefix_mult[-1] * nums[i])
        for i in reversed(range(len(nums))):
            if i==len(nums)-1:
                surfix_mult.append(nums[i])
            else:
                surfix_mult.append(surfix_mult[-1] * nums[i])
        print(prefix_mult)
        print(surfix_mult)
        
        res =[]
        for i in range(len(nums)):
            left_sum = (prefix_mult[i-1] if i !=0 else 1)
            right_sum = (surfix_mult[len(nums) -1 - i - 1] if i !=len(nums)-1 else 1)
            print(f"{i},{left_sum} * {right_sum}")
            res.append(left_sum * right_sum)
        return res


s = Solution()

nums = [1,2,3,4]
print(s.productExceptSelf(nums))