from collections import deque
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k  % len(nums)
        d = deque(nums)
        for i in range(k):
            _ = d[-1]
            d.pop()
            d.appendleft(_)
            # print(d)
        nums[:] = list(d)

nums = [1,2,3,4,5,6,7];k = 3;
s = Solution()

s.rotate(nums=nums,k=k)
print(nums)