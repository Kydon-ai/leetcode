from functions import timer

class Solution:
    @timer
    def minWindow(self, s: str, t: str) -> str:
        i_left,i_right = 0,0
        recoder_dict = dict()
        origin_dict = dict()

        min_length = 0x0f0f0f0f0f
        res_str = ""
        for i in t:
            origin_dict[i] = origin_dict.get(i,0) + 1
        recoder_dict[s[0]] = 1
        while i_left < len(s) and i_right < len(s):
            
            # print(f"当前坐标：({i_left}，{i_right})")
            # print(f"origin:\n{origin_dict}")
            # print(f"recoder:\n{recoder_dict}")
            if not self.check_current(recoder_dict,origin_dict) :
                i_right +=1
                if i_right >= len(s):
                    break
                recoder_dict[s[i_right]] = recoder_dict.get(s[i_right],0) +1
            else:
                # print("准备收缩")
                if min_length > i_right - i_left +1:
                    min_length = i_right - i_left +1
                    res_str = s[i_left:i_right+1]
                recoder_dict[s[i_left]] -=1
                i_left+=1
            
        # print(f'min_length:{min_length}')
        return res_str

    def check_current(self,dict1:dict[str,int],dict2:dict[str,int]) -> bool:
        for key in dict2:
            if dict2[key] > dict1.get(key,0):
                return False
        return True



s = Solution()
# strs = "ADOBECODEBANC"; t = "ABC";
strs = "a"; t = "a";
# strs = "a"; t = "aa";

print(s.minWindow(s=strs,t=t))