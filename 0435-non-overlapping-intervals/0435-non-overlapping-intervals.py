class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[1])
        curr = intervals[0][1]
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= curr:
                curr = intervals[i][1]
            else:
                ans += 1
        return ans