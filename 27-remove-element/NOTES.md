First Approach
```
class Solution:
def removeElement(self, nums: List[int], val: int) -> int:
n = len(nums)
if n == 1:
return 0 if nums[0] == val else 1
l = 0
i = 0
while i < n-l:
if nums[i] == val:
nums.pop(i)
l += 1
continue
i += 1
return len(nums)
```