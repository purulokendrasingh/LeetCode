class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda a: a[1])
        end = -1000000
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            else:
                ans += 1
                print(i)
        return ans