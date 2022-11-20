class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals = sorted(intervals, reverse = True)
        start = float('inf')
        for i in intervals:
            if i[1] <= start:
                start = i[0]
            else:
                ans += 1
        return ans