class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1 or n == 2:
            return n
        ans = 0
        for i in range(n):
            slopes = defaultdict(list)
            for j in range(n):
                if j == i:
                    continue
                xint = points[j][0] - points[i][0]
                if xint != 0:
                    s = (points[j][1] - points[i][1])/(xint)
                    if points[i] not in slopes[s]:
                        slopes[s].append(points[i])
                    if points[j] not in slopes[s]:
                        slopes[s].append(points[j])
                else:
                    s = 'INF'
                    if points[i] not in slopes[s]:
                        slopes[s].append(points[i])
                    if points[j] not in slopes[s]:
                        slopes[s].append(points[j])
            ans = max(ans, max([len(i) for i in slopes.values()]))
        return ans