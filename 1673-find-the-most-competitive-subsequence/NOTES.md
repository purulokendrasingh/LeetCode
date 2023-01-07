TLE Solution:
```
n = len(nums)
arr = [(nums[i], i) for i in range(n)]
heapq.heapify(arr)
ans = []
temp = []
cnt = 0
while cnt < k:
if not arr:
break
t = heapq.heappop(arr)
# print(t, cnt)
if t[1] <= n-k+cnt and (not ans or ans[-1][1] < t[1]):
ans.append(t)
arr.extend(temp)
heapq.heapify(arr)
temp = []
cnt += 1
else:
temp.append(t)
# print(ans)
return [i[0] for i in ans]
```