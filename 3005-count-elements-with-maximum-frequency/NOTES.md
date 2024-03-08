Counter Solution:
```
class Solution:
def maxFrequencyElements(self, nums: List[int]) -> int:
c = Counter(nums)
temp = 0
ans = 0
for k,v in c.most_common():
if temp == 0:
temp = v
ans += 1
elif v == temp:
ans += 1
else:
break
return ans*temp
```