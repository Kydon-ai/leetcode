from collections import deque
from functions import timer

class Solution:
    @timer
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        dq = deque()
        for index in range(len(nums)):

            while len(dq) and dq[0] < index-k+1:
                dq.popleft()
            while len(dq) and nums[dq[-1]] < nums[index]:
                dq.pop()
            dq.append(index)

            if index >=k-1:
                res.append(nums[dq[0]])
        return res


s = Solution()
nums = [1,3,-1,-3,5,3,6,7]; k = 3;
# nums = [1]; k = 1;
# nums = [1,-1]; k =1;
print(s.maxSlidingWindow(nums,k))