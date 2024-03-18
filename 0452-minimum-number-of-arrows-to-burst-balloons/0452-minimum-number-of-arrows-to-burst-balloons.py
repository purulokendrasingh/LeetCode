class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda a: a[1])
        ans = 1
        curr_end = points[0][1]
        for i in points:
            if i[0] > curr_end:
                curr_end = i[1]
                ans += 1
        return ans