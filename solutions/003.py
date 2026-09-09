from functions import timer

class Solution:
    @timer
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_index,right_index = 0,0
        max_len = 0
        my_set = set()
        for right_index in range(len(s)):
            if s[right_index] not in my_set:
                my_set.add(s[right_index])
                if len(my_set) > max_len:
                    max_len = len(my_set) 
            else:
                while left_index<right_index and s[right_index] in my_set:
                    my_set.remove(s[left_index])
                    left_index +=1
                else:
                    my_set.add(s[right_index])
            # print(my_set)
        return max_len




s = Solution()

input_s = "abcabcbb"

print(s.lengthOfLongestSubstring(input_s))