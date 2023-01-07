```
class Solution:
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
n = len(gas)
for i in range(n):
isValid = True
idx = i
excess = 0
for j in range(n):
if idx == n:
idx = 0
if excess + gas[idx] < cost[idx]:
isValid = False
break
else:
excess += gas[idx] - cost[idx]
idx += 1
if isValid:
return i
return -1
```