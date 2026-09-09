class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        recoder_dict:dict[int,int | None] = dict()
        for index,num in enumerate(nums):
            if num in recoder_dict :
                return [index,recoder_dict[num]]
            recoder_dict[target - num] = index


test_list1,target = [1,2,3,4,5,6],11

s = Solution()
print(s.twoSum(test_list1,target))
