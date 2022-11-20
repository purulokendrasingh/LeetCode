class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals = sorted(intervals, reverse = True)
        start = 1000000
        for i in intervals:
            if i[1] <= start:
                start = i[0]
            else:
                print(i)
                ans += 1
        return ans