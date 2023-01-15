NAIVE SOLUTION (TLE):
```
class Solution:
def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
n = len(vals)
c = Counter(vals)
g = defaultdict(list)
for u,v in edges:
g[u].append(v)
g[v].append(u)
ans = 0
for i in range(n):
if c[vals[i]] == 1:
continue
vis = [False]*n
q = deque()
q.append(i)
vis[i] = True
while q:
count = len(q)
for _ in range(count):
temp = q.popleft()
for u in g[temp]:
if not vis[u] and vals[u] <= vals[i]:
vis[u] = True
q.append(u)
if vals[u] == vals[i] and i < u:
ans += 1
elif not vis[u]:
vis[u] = True
return ans+sum(c.values())
```