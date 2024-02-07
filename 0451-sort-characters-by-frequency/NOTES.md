Counter approach:
```
class Solution:
def frequencySort(self, s: str) -> str:
c = Counter(s)
items = sorted(c.items(), key=lambda item: -item[1])
ans = ''
for k,v in items:
ans += k*v
return ans
```