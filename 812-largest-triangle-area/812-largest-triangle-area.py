class Solution:
    def largestTriangleArea(self, p: List[List[int]]) -> float:
        n = len(p)
        ans = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    area = 0.5*abs(p[i][0]*(p[j][1]-p[k][1]) + p[j][0]*(p[k][1]-p[i][1]) + p[k][0]*(p[i][1]-p[j][1]))
                    ans = max(ans, area)
        return ans