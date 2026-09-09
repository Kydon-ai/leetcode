from functions import timer


class Solution:
    @timer
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p,p_len = sorted(p),len(p)

        res = []
        for i in range(0,len(s)-len(p)+1):
            tmp_str = sorted(s[i:i+p_len])
            # print(f"{p},{tmp_str}")
            if tmp_str == p:
                res.append(i)
        return res
        

s = Solution()
strs,p = "cbaebabacd","abc"

# strs,p = "abab", "ab"
print(s.findAnagrams(s=strs,p=p))