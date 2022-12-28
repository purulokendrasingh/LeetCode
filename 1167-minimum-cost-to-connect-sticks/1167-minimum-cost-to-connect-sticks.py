class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        n = len(sticks)
        if n == 1:
            return 0
        sticks.sort()
        a = deque(sticks)
        ans = 0
        for _ in range(n-1):
            temp = a[0] + a[1]
            a.popleft()
            a.popleft()
            bisect.insort(a, temp)
            ans += temp
        return ans