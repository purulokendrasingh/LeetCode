```
indeg = [False]*n
for u,v in edges:
if not indeg[v]:
indeg[v] = True
ll = []
for i in range(n):
if not indeg[i]:
ll.append(i)
return ll
```