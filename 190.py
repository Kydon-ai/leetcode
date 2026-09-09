class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:].zfill(32)[::-1]
        return int(n,base=2)


s = Solution()
n = 43261596

print(s.reverseBits(n))