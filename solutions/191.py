class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)[2:].zfill(32)
        return sum([i=='1' for i in s])

s = Solution()
n = 11
print(s.hammingWeight(n))