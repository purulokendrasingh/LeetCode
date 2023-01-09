Naive Solution:
```
class Solution:
def validSubarrays(self, nums: List[int]) -> int:
n = len(nums)
ans = 0
for i in range(n):
for j in range(i, n):
if i == j:
ans += 1
continue
if nums[i] <= nums[j]:
ans += 1
else:
break
return ans
```