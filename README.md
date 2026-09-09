# 基础
根据数据范围估算算法对于Py程序的复杂度要求

| 时间复杂度 | n=10³ | n=10⁴ | n=10⁵ | n=10⁶ |
| :--- | :---: | :---: | :---: | :---: |
| O(1) | ✅ | ✅ | ✅ | ✅ |
| O(log n) | ✅ | ✅ | ✅ | ✅ |
| O(n) | ✅ | ✅ | ✅ | ✅ (注意常数) |
| O(n log n) | ✅ | ✅ | ✅ | ⚠️ (勉强) |
| O(n²) | ✅ | ✅ | ❌ | ❌ |
| O(n³) | ✅ | ❌ | ❌ | ❌ |
| O(2ⁿ) | ✅ (n≤20) | ❌ | ❌ | ❌ |
| O(n!) | ✅ (n≤10) | ❌ | ❌ | ❌ |

# 1.两数之和

> 链接：https://leetcode.cn/problems/two-sum/?envType=study-plan-v2&envId=top-100-liked

## 思路
暴力思路：两个循环分别指向数组中的两个不同位置，分别遍历
题解思路：每遍历一个数据，可以知道当前哪个数据已经被遍历，而遍历到后续的数据时，可以通过**哈希表**将以存在的数据以平均O(1)的速度快速查找是否存在，这样就可以等效以接近O(n)的速度判断当前位置的前置互补数字是否存在。

## 代码
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        recoder_dict:dict[int,int] = dict()
        for index,num in enumerate(nums):
            if num in recoder_dict :
                return [index,recoder_dict[num]]
            recoder_dict[target - num] = index
```

# 2.字母异位词分组

> 链接：https://leetcode.cn/problems/group-anagrams/?envType=study-plan-v2&envId=top-100-liked

## 思路
直接将每个字符串按照字典序排序作为key，然后通过该key作为索引收集对应的异位词即可，最后遍历该字典返回对应列表
> str.sort()是原地操作，而sorted(str)是会返回新的字符串

## 代码
```python
class Solution:
    def getSortedStr(self,s:str):
        return "".join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict将“检查键是否存在”和“为不存在的键设置初始值”这两个步骤合并了
        myDict:Dict[str,List[str]] = defaultdict(list)
        for i in strs:
            # myDict[self.getSortedStr(i)].append(i)
            # key = "".join(sorted(i))
            key = self.getSortedStr(i)
            
            myDict[key].append(i)
        # 直接调用list() 和values方法
        return list(myDict.values())
```

# 3.最长连续序列

> 链接：https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
类似于桶排序的思路，将所有的数据先记录下来，然后从最小下标开始一个一个遍历，找出最长的连续序列区间长度。不同的是使用set可以自动哈希记录到表上，索引只需要平均O(1)。于是我们随机遍历set，总会访问到最长的起始数字，最差的情况下为O(n^2)也足够

## 代码
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        if not len(nums):
            return res
        # 使用hash记录哪些数据num在，并且根据num-1判断是否要开始遍历一整个区间
        # 根本不需要Dict
        mySet:Set[int] = set(nums)

        for i in mySet:
            if i-1 in mySet or i not in mySet:
                continue
            index = i
            while(index in mySet):
                index+=1
                # print("{}存在".format(index))
            res = max(res,index - i)
            if res * 2 >= len(nums) :
                return res
        return res
```

# 4.移动零

> 链接：https://leetcode.cn/problems/move-zeroes/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
因为数组的赋值，切片，交换等操作都是原地操作，所以我们保持一个指向当前数组最前方的一个0的下标的前方指针，每次遍历到非零元素时直接将该元素和前方指针位置的元素进行赋值交换即可。这样就能确保遍历一次最后将0都移动到末尾
## 代码
```python
class Solution:
    def find_first_zero(self,nums: List[int]):
        for index,value  in enumerate(nums):
            if not value:
                return index
        return -1
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        empty_index = self.find_first_zero(nums)
        if empty_index is -1:
            return 
        for index,value in enumerate(nums):
            if value and empty_index < index:
                nums[empty_index] = value
                nums[index] = 0
                empty_index +=1
```
# 5.盛最多水的容器

> 链接：https://leetcode.cn/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
双指针遍历，已知答案必定包含在两端的中间，可以寻找某种移动方法找到这种中间状态的位置。如果设置初始状态为左右两个端点，那么往中间更新的话，由于宽度缩短，必须调整短板方向才能找到更大的答案。但是如何证明该贪心的方案的必定正确性就比较靠直觉。

## 代码
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i_left,i_right = 0,len(height)-1
        sum_max = 0
        while(i_left <i_right):
            temp_res= min(height[i_left],height[i_right]) * (i_right - i_left)
            if (temp_res > sum_max):
                sum_max = temp_res
        
            if height[i_left] <=height[i_right]:
                i_left = i_left + 1  
            else:
                i_right = i_right - 1
        return sum_max
```

# 6.三数之和

> 链接：https://leetcode.cn/problems/3sum/?envType=study-plan-v2&envId=top-100-liked

## 思路
暴力思路：看数据范围，10^3大概可以用O(n^3)，暴力可以过
官方思路：使用三指针法，首先进行升序排序。然后一个中指针进行遍历，另外两个指针分别指向数组开头和结尾，中指针会遍历除两端以外的每个位置，算法复杂度最差接近O(n^2),因为是对0为目标求和，可以利用这一点进行剪枝（最大组合小于0，跳过找后续；最小组合大于0，终止）

## 代码
```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''没要求返回下标，可以考虑排序了'''
        nums: list[int] = sorted(nums)
        res:list[list[int]] = []
        my_set = set()
        for index in range(1, len(nums) - 1):
            i_left,i_right = 0,len(nums)-1
            if nums[0] + nums[index] + nums[index+1] > 0:
                break
            if nums[index-1] + nums[index] + nums[len(nums)-1] < 0:
                continue
            while i_left < index and index < i_right:
                if (nums[i_left] + nums[index] + nums[i_right] ==0):
                    triplet = (nums[i_left], nums[index], nums[i_right]) 
                    if triplet not in my_set:  # 集合查找是 O(1)
                        my_set.add(triplet)
                        res.append([nums[i_left], nums[index], nums[i_right]])
                    del triplet
                    while(nums[i_left+1] == nums[i_left] and i_left < i_right-1):
                        i_left +=1
                    while(nums[i_right-1] == nums[i_right] and i_left < i_right-1):
                        i_right -=1
                    
                    i_left +=1
                    i_right -=1
                elif (nums[i_left] + nums[index] + nums[i_right] >0):
                    i_right -=1
                else:
                    i_left +=1
        return res
```
# 7.接雨水

> 链接：https://leetcode.cn/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
个人思路：横向扫描法，遍历每个高度，如果有两个以上的高度达到，那么则计算这些间隔之间的间隙之和，时间复杂度为O(h*n)
官方思路1：前缀和（动态规划），分别两次遍历记录每个位置左边前缀和的最大高度和右边前缀和的最大高度。而每个位置从纵向看，能装的水=max(min(左侧最大高度,右侧最大高度)-当前高度,0)。相当于纵向扫描法
官方思路2：单调栈（递减栈），每次找到一个递增的，将其退栈到同等高度。过程中添加当前元素与退栈元素的距离。相当于分段横向扫描法
## 代码
```python
class Solution:
    def trap(self, heights: list[int]) -> int:
        water_capacity = 0
        left_max,right_max = 0,0
        left_max_lists,right_max_lists = [],[]
        # 使用前缀和，非一般地体验！
        for indexs in range(len(heights)):
            left_max = max(heights[indexs],left_max)
            left_max_lists.append(left_max)

        for indexs in reversed(range(len(heights))):
            right_max = max(heights[indexs],right_max)
            right_max_lists.append(right_max)
        
        del left_max
        del right_max

        for index in range(1,len(heights)-1):
            left_max,right_max = left_max_lists[index],right_max_lists[len(heights)-1-index]
            water_capacity +=  max(0,min(left_max,right_max) - heights[index])
            # print(f"位置：{index},高度：{heights[index]}，容量线：{min(left_max,right_max)}，增添：{max(0,min(left_max,right_max) - heights[index])}")
        return water_capacity
```

# 8.无重复字符的最长子串

> 链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
双指针法，同时初始化到数组开头位置。如果尾部指针遍历到重复元素，则更新头部指针到没有重复元素为止
## 代码
```python
class Solution:
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
```

# 9.找到字符串中所有字母异位词

> 链接：https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
暴力思路：遍历每个位置，截取异位词长度排序，如果是异位词则加入下标进答案
官方思路：维护一个哈希计数表，如果计数表和目标词一致，则加入前len(target)作为下标进入数组
## 代码
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p,p_len = sorted(p),len(p)

        res = []
        for i in range(0,len(s)-len(p)+1):
            tmp_str = sorted(s[i:i+p_len])
            # print(f"{p},{tmp_str}")
            if tmp_str == p:
                res.append(i)
        return res
```
# 10.和为 K 的子数组

> 链接：https://leetcode.cn/problems/subarray-sum-equals-k/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
通过前缀和，记录每个和的出现次数。每次遍历时累加target-current_num的出现次数
## 代码
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum:list[int] = []
        res = 0;
        for index,num in enumerate(nums):
            if index == 0:
                prefix_sum.append(num)
            else:
                prefix_sum.append(prefix_sum[index-1] + num)
        
        recoder_lists:dict[int,int] = dict({0:1})

        for i in range(len(prefix_sum)):
            if (prefix_sum[i] - k ) in recoder_lists :
                res +=recoder_lists[prefix_sum[i] - k ]
            recoder_lists[prefix_sum[i]] = recoder_lists.get(prefix_sum[i],0) + 1

        return res
```


# 11.滑动窗口最大值

> 链接：https://leetcode.cn/problems/sliding-window-maximum/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

利用双端队列，存储每个值的下标进入该队列。每个数进来时，保持队首的最大值没有过期，从末尾pop比他小的数字，将其加入进队列尾部。当遍历到超出窗口size的时候，加入此时的队首即为答案序列。

## 代码

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
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
```



# 12.最小覆盖子串



> 链接：https://leetcode.cn/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

本题和“无重复字符的最长子串”思路一致，使用双指针初始化到开头，利用哈希表记录当前是否满足覆盖要求。不满足要求扩充右边界，满足要求则更新答案并收缩左边界直到不满足要求



## 代码

```python
class Solution:
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
```



# 13.最大子数组和

> 链接：

## 思路

经典的**Kadane's**算法，第一次做没了解，用双指针写遍历，边界移动条件怎么改都不对。思路是动态规划，要么加上上一个元素，如果过往的这一段不如当前则直接采用当前数字。结果就是这个过程中的每个结果的最大值。

## 代码

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        current_max = 0
        if len(nums) == 1:
            return global_max
        for num in nums:
            current_max = max(num,current_max + num)
            global_max = max(current_max,global_max)
        return global_max
```

# 14.合并区间

> 链接：https://leetcode.cn/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-100-liked



## 思路

看数据范围，最大支持O(N^2),那么先来一次排序，按照区间左边界进行排序。如果新来的区间的左区间有覆盖，那么则进行合并，否则直接将目前维护好的区间加入答案序列。需要注意合并区间时的边界问题。复杂度大概为O(nlogn)由排序决定，主处理流程为O(n)



## 代码

```python
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []
        intervals.sort(key=lambda x :x[0])
        current_tuple = None
        for interval in intervals:
            if not current_tuple:
                current_tuple = interval
            else:
                if interval[0] > current_tuple[1]:
                    res.append(current_tuple)
                    current_tuple = interval
                else:
                    current_tuple = self.merge2(current_tuple,interval)
        res.append(current_tuple)
        return res
    def merge2(self,current_tuple,interval):
        return [current_tuple[0],max(current_tuple[1],interval[1])]
```

# 15.轮转数组

> 链接：https://leetcode.cn/problems/rotate-array/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

双端队列直接队首队尾轮转操作即可，记得取余

## 代码

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k  % len(nums)
        d = deque(nums)
        for i in range(k):
            _ = d[-1]
            d.pop()
            d.appendleft(_)
            # print(d)
        nums[:] = list(d)
        
```

# 16.除了自身以外数组的乘积

> 链接：https://leetcode.cn/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

题目标签里有前缀和，想到记录左向的前缀累乘和右向的前缀累乘，答案就是当前位置左边的前缀累乘和右边的前缀累乘的成绩（不过时间和空间复杂度常数太大了）

## 代码

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
        
        res =[]
        for i in range(len(nums)):
            left_sum = (prefix_mult[i-1] if i !=0 else 1)
            right_sum = (surfix_mult[len(nums) -1 - i - 1] if i !=len(nums)-1 else 1)
            print(f"{i},{left_sum} * {right_sum}")
            res.append(left_sum * right_sum)
        return res
```



# 17.缺失的第一个正数

> 链接：https://leetcode.cn/problems/first-missing-positive/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

看数据范围，负数不动，超出1e5+1的数也不管（因为最多1e5个正整数，当然我这里用了nums的长度就行了）。遍历每个数，如果是符合范围的数字，将其交换到对应下标位置（通过赋值操作），否则不动。最后在遍历一次就能排查出哪个最小的正数没出现

## 代码

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while (nums[i] >=1  and nums[i] != i+1 and nums[i]<=N  and nums[nums[i]-1] !=nums[i]):
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        # print(nums)
        for i in range(N):
            if (nums[i] != i+1):
                return i+1
        return N+1
        
```



# 18.矩阵置零

> 链接：https://leetcode.cn/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

扫描每个元素，分别记录有0的行和列分别的编号

最后两个双重循环（数据范围很小）将对应的行列置零

## 代码

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        line,col = len(matrix),len(matrix[0])
        line_lists = [False for _ in range(line)]
        col_lists = [False for _ in range(col)]
        
        for i in range(line):
            for j in range(col):
                if matrix[i][j] == 0:
                    line_lists[i] = True
                    col_lists[j] = True
        for i in range(line):
            if line_lists[i]:
                for j in range(col):
                    matrix[i][j] = 0
        for i in range(col):
            if col_lists[i]:
                for j in range(line):
                    matrix[j][i] = 0
        
```

# 19.螺旋矩阵

> 链接：https://leetcode.cn/problems/spiral-matrix/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

创建一个函数，从左上角开始顺时针读取一个矩阵最外侧的数字将其加入队列。每次收缩行列序号切片传入，注意处理好单行和单列的情况即可。（不得不说数据比较水）

## 代码

```python
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        line_top,line_bottom = 0,len(matrix)-1
        col_left,col_right = 0,len(matrix[0])-1

        while line_top <=line_bottom and col_left<=col_right:
            res.extend(self.get_next([line[col_left:col_right+1] for line in matrix[line_top:line_bottom+1] ]))
            line_top +=1
            line_bottom -=1
            col_left +=1
            col_right -=1
        return res
    
    def get_next(self,matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix:
            return res
        if len(matrix) ==1:
            return matrix[0]
        if len(matrix[0])==1:
            for i in matrix:
                res.append(i[0])
            return res
        for i in range(len(matrix[0])):
            if i== len(matrix[0])-1:
                break
            res.append(matrix[0][i])
        for i in range(len(matrix)):
            if i== len(matrix)-1:
                break
            res.append(matrix[i][-1])
        for i in reversed(range(len(matrix[0]))):
            if i ==0:
                break
            res.append(matrix[-1][i])
        for i in reversed(range(len(matrix))):
            if i ==0:
                break
            res.append(matrix[i][0])
        return res
```

# 20.旋转图像

> 链接：https://leetcode.cn/problems/rotate-image/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

先沿主对角线对称交换，然后沿中心纵列对称交换

## 代码

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                matrix[i][j],matrix[i][len(matrix[0])-j-1] = matrix[i][len(matrix[0])-j-1],matrix[i][j]
        # print(matrix)
        
```

# 21.搜索二维矩阵 II

> 链接：https://leetcode.cn/problems/search-a-2d-matrix-ii/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

一开始以为可以从主对角线从右下角往左上角遍历确定一个小遍历区间，这样做总是有遗漏的，且选取的空间范围太大。其实是一颗二叉搜索树，从右上角看，左边的都比他小，右边的都比他大。也可以反过来从左下角看

## 代码

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        start_x ,start_y = 0,len(matrix[0])-1
        res = False
        while matrix[start_x][start_y] != target:
            if matrix[start_x][start_y] >target:
                start_y -=1
            else:
                start_x +=1
            
            if start_y <0 or start_x >=len(matrix):
                break
        else:
            res = True
        return res
```

# 22.相交链表

> 链接：https://leetcode.cn/problems/intersection-of-two-linked-lists/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

两个指针，分别指向a和b，其中每个指针走完之后都从另一个指针头开始再走一遍，第二次相遇时，直接返回节点（默认最多也只会分别遍历两次）

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_copy,b_copy = headA,headB

        while headA or headB:
            if headA == headB:
                
                return headA
            
            if headA == None:
                headA = b_copy
                continue
            if headB == None:
                headB = a_copy
                continue
            
            headA = headA.next
            headB = headB.next
        else:
            return None

        
```



# 23.反转链表

> 链接：https://leetcode.cn/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

每次遍历，保存上个节点的指针，将next指向前驱节点，最后返回最后一个节点的引用

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p = head
        head = head.next 
        p.next = None
        while head:
            t = head
            head = head.next
            t.next = p
            p = t
        else:
            return p
```

# 24.回文链表

> 链接：https://leetcode.cn/problems/palindrome-linked-list/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

根据之前的反转链表，获取其反转，然后同时遍历，如果元素值不一样则返回False，否则最后返回True

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = head
        pr = self.get_reverse_link(copy.deepcopy(head))
        while p and pr:
            print(p.val," ",pr.val)
            if p.val !=pr.val:
                return False
            p = p.next
            pr = pr.next
        return True


    def get_reverse_link(self,head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p = head
        head = head.next
        p.next = None
        while head:
            _ = head
            head = head.next
            _.next = p
            p = _
        else:
            return p

        
```

# 25.环形链表

> 链接：https://leetcode.cn/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

使用快慢指针，如果走两倍长度，要么快指针直接终止无环；要么会相遇，有环

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False 
        max_N = 3e4 // 1
        slow = fast = head 
        fast = fast.next
        while max_N and fast:
            max_N -=1
            if fast == slow:
                return True
            if fast.next:
                fast = fast.next.next
                slow= slow.next
            else:
                break
        return False
```

# 26.环形链表 II

> 链接：https://leetcode.cn/problems/linked-list-cycle-ii/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

和上题一样，只不过返回值是节点的引用地址

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None 
        max_N = 3e4 // 1
        slow = fast = head
        while max_N and fast:
            max_N -=1
            if fast.next:
                fast = fast.next.next
                slow= slow.next
            else:
                return None
            if fast == slow:
                break
        else:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
            if slow == head:
                return head
        else:
            return head
        
        
```



# 27.合并两个有序链表

> 链接：https://leetcode.cn/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

两个指针遍历，哪个值大就将哪个指针加入新链表，直到两个指针都为None，然后返回新链表头节点

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p_copy= p = ListNode()
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    p.next = list1
                    list1 = list1.next
                else:
                    p.next = list2
                    list2 = list2.next
            else:
                if list1:
                    p.next = list1
                    list1 = list1.next
                else:
                    p.next = list2
                    list2 = list2.next
            p = p.next
        
        return p_copy.next
        
```

# 28.两数相加

> 链接:https://leetcode.cn/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

像算数加法竖式那样，准备好进位即可

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        jinwei = 0
        p = res = ListNode()
        while l1 or l2:
            if l1 and l2:
                res.next = ListNode((l1.val + l2.val  + jinwei) %10)
                jinwei = (l1.val + l2.val  + jinwei) // 10
            else:
                if l1:
                    res.next = ListNode((l1.val+ jinwei) %10)
                    jinwei = (l1.val  + jinwei) // 10
                else:
                    res.next = ListNode((l2.val  + jinwei) %10)
                    jinwei = (l2.val  + jinwei) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res = res.next
        if jinwei:
            res.next = ListNode(jinwei %10)
        return p.next

        
```



# 29.删除链表的倒数第 N 个结点

> 链接：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

先初始化pre和tail两个节点，先让tail走n个节点，然后等tail走到终点，这样pre附近就走到了需要删除的结点附近，就可以开始删除了

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre = tail = head
        for i in range(n+1):
            if tail:
                tail = tail.next 
            else:
                return head.next
        while tail:
            tail = tail.next
            pre = pre.next
        else:
            pre.next = pre.next.next if  pre.next else None
        return head

        
```

# 30.两两交换链表中的节点

> 链接：https://leetcode.cn/problems/swap-nodes-in-pairs/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

使用以前一后两个指针，每次都走两步，交换这两个节点的顺序即可

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        pre = post = head
        copy_p = post = post.next
        if not post:
            return pre
        prepre = None
        while post:
            if prepre:
                prepre.next = post
            pre.next = post.next
            prepre = post.next = pre

            post = pre.next.next if pre.next else None
            pre = pre.next
            
        else:
            return copy_p
        
        
```

# 31.K 个一组翻转链表

> 链接：https://leetcode.cn/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

实现一个函数，传入起始和结束节点的引用位置，返回反转后这部分的head和tail，外部循环拼接起来。最后返回头节点

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        p0 = ListNode()
        p0.next = head
        pp = h = t = p = p0
        pre = pp
        pp = pp.next
        while pp:
            h = pp
            for i in range(k):
                if i == k-1:
                    t = pp
                if pp:
                    pp = pp.next 
                else:
                    return p0.next
            new_head,new_tail = self.reverse_part(h,t)
            pre.next = new_head
            new_tail.next = pp
            pre = new_tail
            # print("查看转换：",pre.val,new_head.val,new_tail.val,new_tail.next)
            # print("中途print:",p0.next)
        return p0.next
    
    def reverse_part(self,head: Optional[ListNode],tail: Optional[ListNode])-> tuple[Optional[ListNode],Optional[ListNode]]:
        # print("进入节点：",head.val,tail.val)
        p = head
        stop = tail.next
        pre,current = head,head.next
        while current !=stop:
            # print(f"当前current：{current.val},{tail.val}")
            _ = current.next
            current.next= pre
            pre,current = current,_

        return pre,p
```

## 32.随机链表的复制

> 链接：https://leetcode.cn/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

本题要求进行深拷贝，那么则必须能够再手动构造节点。因为需要复制random指针，那么因为不知道random的具体数值，但是我们知道我们迟早会遍历到这些random指向的节点，必须先将每个每个节点的映射记录下来，我们就采用id()作为节点的key，后续添加新节点的random时，根据映射快速进行创造和添加

## 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p = p0 = p1 = Node(-1)
        h = h0 = h1 = head
        node_dict:dict[int,'Optional[Node]'] = dict()
        while head:
            p1.next = self.get_copy_node(head,node_dict)
            head = head.next
            p1 = p1.next
        p0 = p0.next
        # print(f"查看hash:{node_dict}")
        while p0 and h1:
            if h1.random:
                p0.random = node_dict[id(h1.random)]
            else:
                p0.random = None
            p0= p0.next
            h1 = h1.next
        return p.next

    def get_copy_node(self,head: 'Optional[Node]',node_dict:dict[str,'Optional[Node]'])-> 'Optional[Node]':
        node = Node(x = head.val)
        node_dict[id(head)] = node
        return node
        
```

# 33.排序链表

> 链接：https://leetcode.cn/problems/sort-list/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

题目要求O(nlogn)，那么可以使用归并排序而不是冒泡。归并排序要求找到中点，我们使用快慢指针，从慢指针那里开始断开，将head和mid开始的链表继续切分，直到只有一个元素。这样返回两个有序列表，再走有序列表的合并，返回最终的头节点即可

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        slow , fast = head,head.next
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next
        mid , slow.next = slow.next,None
        left_start ,right_start =  self.sortList(head),self.sortList(mid)
        return self.mergeTwoLists(left_start,right_start)

    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p_copy= p = ListNode()
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    p.next = list1
                    list1 = list1.next
                else:
                    p.next = list2
                    list2 = list2.next
            else:
                if list1:
                    p.next = list1
                    list1 = list1.next
                else:
                    p.next = list2
                    list2 = list2.next
            p = p.next
        
        return p_copy.next
```

# 34.合并 K 个升序链表

> 链接：https://leetcode.cn/problems/merge-k-sorted-lists/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

个人思路：使用优先队列，将所有数值都加入进去排序好，然后从小到大遍历出队

官方思路1：暴力合并，看成n-1个有序列表合并

官方思路2：优先队列，但是维护的是每个链表最前面没有被合并的一个

## 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()
        count = 0
        for node in lists:
            while node:
                pq.put((node.val,count,node))
                count +=1
                node = node.next
        p = head = ListNode()
        while not pq.empty():
            num,_,node = pq.get()
            # print(num)
            head.next = node
            head = head.next
        return p.next
```

# 35.LRU 缓存

> 链接：https://leetcode.cn/problems/lru-cache/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

使用双向虚拟头循环列表来表示，并使用key和Node的映射来快速获取某个元素是否在链表中或者具体引用

添加就是删除旧的加入同样的元素到头部，如果容量不够则从末尾删除

删除就是删除某个节点

## 代码

```python
class LinkList:
    def __init__(self,key:int=0,value:int=0,next:LinkList | None=None,pre:LinkList | None=None):
        self.value = value
        self.key = key
        self.next = next
        self.pre = pre
    @classmethod
    def create_empty_link(cls):
        a,b = cls(),cls()
        a.next=b;a.pre=b
        b.next=a;b.pre=a
        return a,b

class LRUCache:
    def __init__(self, capacity: int):
        self.head,self.tail = LinkList.create_empty_link()
        self.capacity = capacity
        self.size = 0
        self.recoder = dict() #  int -> LinkList

    def get(self, key: int) -> int:
        node:LinkList|None = self.recoder.get(key,None)
        if node:
            self.remove_node(node)
            self.add_node(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        new_node = LinkList(key,value)
        old_node = self.recoder.get(key,None)
        if old_node:
            self.remove_node(old_node)
        self.add_node(new_node)

        if self.size > self.capacity:
            self.remove_node(self.tail.pre)
        

    def remove_node(self,head:LinkList) -> None:
        pre,next = head.pre,head.next
        pre.next = next
        next.pre = pre
        self.size -=1
        del self.recoder[head.key]
        del head
    
    def add_node(self,node:LinkList) ->None:
        pre,next = self.head,self.head.next
        pre.next = node;node.next=next
        next.pre = node;node.pre=pre
        self.size +=1
        self.recoder[node.key] = node
```

# 36.二叉树的中序遍历

> 链接：https://leetcode.cn/problems/binary-tree-inorder-traversal/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

中序遍历，则左-根-右即可

## 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traversal(res,root)
        return res

    def traversal(self,res:list[int],root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.traversal(res,root.left) if root.left else None
        res.append(root.val)
        self.traversal(res,root.right) if root.right else None
        
```

# 37.二叉树的最大深度

> 链接：https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked

## 思路

每次遍历时带层数下去即可，全局维护该最大层数作为结果

## 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.traversal(1,root)
        return self.res
    
    def traversal(self,lay_count:int,root:Optional[TreeNode]) ->None:
        if root is None:
            return 
        if lay_count>self.res:
            self.res = lay_count

        self.traversal(lay_count+1,root.left) if root.left else None
        self.traversal(lay_count+1,root.right) if root.right else None
        
        
```

# 38.翻转二叉树
> 链接：https://leetcode.cn/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-100-liked

## 思路
任意一种二叉树遍历方式，然后直接交换左右子树

## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverse_tree(root)
        return root
    
    def reverse_tree(self,root:Optional[TreeNode]) -> None:
        if root is None: return 
        root.left,root.right = root.right,root.left
        self.reverse_tree(root.left) if root.left else None
        self.reverse_tree(root.right) if root.right else None
```
# 39.对称二叉树
> 链接：https://leetcode.cn/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
个人思路：一开始想的是对称翻转后按同样的方式遍历，看是否遍历数值顺序一致。但是如果数值都是一样的，这种方式并不能检测出

官方思路：通过比对两颗子树，看他们彼此的左子树和右子树的节点值是否相等。如果都是对称相等，那么则结构对称且数值相等，那么他们就是对称的二叉树。

## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left,root.right)
    
    def check(self,left:Optional[TreeNode],right:Optional[TreeNode]) -> bool:
        if not left and not right: return True
        if not left or not right: return False
        return left.val == right.val and self.check(left.left,right.right) and self.check(left.right,right.left) 
```

# 40.二叉树的直径
> 链接：https://leetcode.cn/problems/diameter-of-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
直径为最长的两个节点之间的边数，可以观察得到答案为max(左子树最大深度 + 右子树最大深度 - 2*当前深度)
## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.traversal(1,root)
        return self.res
    
    def traversal(self,current_layer:int,root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return current_layer
        else:
            left_max,right_max = current_layer,current_layer
            if root.left:
                left_max = self.traversal(current_layer+1,root.left)
            if root.right:
                right_max = self.traversal(current_layer+1,root.right)
            if left_max + right_max - 2*current_layer > self.res:
                self.res = left_max + right_max - 2*current_layer
            return max(left_max,right_max)
```

# 41.二叉树的层序遍历
> 链接：https://leetcode.cn/problems/binary-tree-level-order-traversal/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
层序遍历只需要使用层数当做二维列表的一级下标即可。考虑到长度不确定，需要动态加入，那么考虑从顶部开始加到底部，前序遍历为比较好的方式。采用其他遍历方式也可以，不过需要实时监测当前层数给列表扩容，我这里采用的是中序。

## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res:list[list[int]] =[]
        self.traversal(1,root)
        return self.res
    
    def traversal(self,layer_num:int,root:Optional[TreeNode]):
        if root is None: return
        if len(self.res) <layer_num:
            self.res.append([])

        self.traversal(layer_num+1,root.left) if root.left else None
        self.res[layer_num-1].append(root.val)
        self.traversal(layer_num+1,root.right) if root.right else None
```

# 42.将有序数组转换为二叉搜索树
> 链接：https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
我们观察到，每个根节点都位于左右子树的中心位置，所以透传整个数组，每次传递左右数组范围，将中间的数值作为节点创建并挂载。如果某次的left和right相等，那么则下一次需要终止

## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums,0,len(nums)-1)
    
    def helper(self,nums:list[int],left:int,right:int) -> Optional[TreeNode] | None:
        if left > right: return None
        mid = (left+right)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums,left,mid-1)
        root.right = self.helper(nums,mid+1,right)

        return root
```
# 43.验证二叉搜索树
> 链接：https://leetcode.cn/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
每个子树根节点，都要根据自身相对父节点的位置满足父节点的要求。而父节点如果经历过左节点，那么会有一个上限，如果经历过右节点，那么会有一个下限。那么我们只需要找到根节点的上下限，然后递归传递每个子树的上下线即可。观察数据范围，确定界限为[(-2)^31-1,2^31]

## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        min_value,max_value = -2**31-1,2**31
        self.traversal_tree(min_value,max_value ,root)
        return self.res
    
    def traversal_tree(self,min_value:int,max_value:int,root: Optional[TreeNode]) -> None:
        if root is None: return 
        if root.val <=min_value or root.val >= max_value:
            self.res = False
        
        self.traversal_tree(min_value,root.val,root.left) if root.left else None
        self.traversal_tree(root.val,max_value,root.right) if root.right else None
```

# 44. 二叉搜索树中第 K 小的元素
> 链接：https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
我们可以发现中序遍历就是二叉搜索树的从小到大排序，所以每次遍历全局计数即可

## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.count = 0
        self.k = k
        self.traversal(root)
        return self.res
    
    def traversal(self,root: Optional[TreeNode]) -> None:
        if root is None: return 
        
        self.traversal(root.left) if root.left else None
        
        self.count +=1
        if self.k == self.count:
            self.res = root.val
        self.traversal(root.right) if root.right else None
```

# 45.二叉树的右视图
> 链接：https://leetcode.cn/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
其实就是层序遍历后的每个子数组的最后一个元素

## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.layer_taversal:list[list[int]] = []
        self.traversal(1,root)
        self.res = []
        
        for a_list in self.layer_taversal:
            self.res.append(a_list[-1])
        
        return self.res

    
    def traversal(self,layer_num:int,root:Optional[TreeNode]) -> None:
        if root is None: return 
        if len(self.layer_taversal) < layer_num:
            self.layer_taversal.append([])
        self.layer_taversal[layer_num-1].append(root.val)

        self.traversal(layer_num+1,root.left) if root.left else None
        self.traversal(layer_num+1,root.right) if root.right else None
```

# 46.二叉树展开为链表
> 链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
根据题目要求，我们发现可以遍历到左节点的时候，将左节点插入到右节点，然后找到该节点的右节点（没有的话就是自身），将这个找到的节点的右节点设置为原先的下一个右节点

## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        p = root
        self.traversal(root)
        return p
    
    def traversal(self,root:Optional[TreeNode]):
        if root is None: return
        
        if root.left:
            right_next = root.right
            if root.left.right:
                last_right = root.left.right
            else:
                last_right = root.left
            while last_right and last_right.right:
                last_right = last_right.right
            
            last_right.right = right_next
            root.right = root.left
            root.left = None

        self.traversal(root.left) if root.left else None
        self.traversal(root.right) if root.right else None
```

# 47.从前序与中序遍历序列构造二叉树
> 链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-100-liked

## 思路
前序给根节点，中序用于划分左右子树。当只剩一个元素时，下一步递归则直接返回。需要使用哈希记录元素到下标的映射，用于快速定位。

## 代码
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.my_recorder = dict()
        for idx,value in enumerate(inorder):
            self.my_recorder[value] = idx
        
        self.preorder,self.inorder = preorder,inorder
        return self.get_tree(0,len(preorder)-1,0,len(inorder)-1)
    
    def get_tree(self,pl:int,pr:int,il:int,ir:int) -> Optional[TreeNode]:
        if pl>pr: return
        
        inorder_root_idx = self.my_recorder[self.preorder[pl]]
        l_len = inorder_root_idx - il
        root = TreeNode(self.preorder[pl])
        root.left = self.get_tree(pl+1,pl+l_len,il,inorder_root_idx-1)
        root.right = self.get_tree(pl+l_len+1,pr,inorder_root_idx+1,ir)
        
        return root
```

# 48.