Dictionary Method:
```
class Solution:
def containsDuplicate(self, nums: List[int]) -> bool:
vis = defaultdict(bool)
for num in nums:
if vis[num]:
return True
vis[num] = True
return False
```