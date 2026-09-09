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


s = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals =[[1,4],[5,6]]
intervals = [[1,4],[0,0]]
intervals = [[1,4],[2,3]]
print(s.merge(intervals))