DP solution:
```
class Solution:
def minimumRounds(self, tasks: List[int]) -> int:
counts = Counter(tasks).values()
if 1 in counts:
return -1
dp = defaultdict(lambda: None)
def helper(n):
if dp[n] != None:
return dp[n]
if n == 0:
dp[n] = 0
elif n < 0:
dp[n] = 100000
else:
dp[n] = min(1 + helper(n-3), 1 + helper(n-2))
return dp[n]
ans = 0
for i in counts:
ans += helper(i)
return ans
```