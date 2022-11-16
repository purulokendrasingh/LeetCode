Alt. Solution (TLE):
```
class Solution:
def countPrimes(self, n: int) -> int:
if n <= 2:
return 0
def prime(x):
i = 2
while i*i <= x:
if x%i == 0:
return False
i += 1
return True
return sum([prime(i) for i in range(1,n,2)])
```