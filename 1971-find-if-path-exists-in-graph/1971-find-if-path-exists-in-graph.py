class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        d = defaultdict(list)
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        q = deque()
        q.append(source)
        vis = defaultdict(bool)
        vis[source] = True
        while q:
            c = len(q)
            for i in range(c):
                temp = q.popleft()
                for j in d[temp]:
                    if vis[j]:
                        continue
                    elif j == destination:
                        return True
                    else:
                        vis[j] = True
                        q.append(j)
        return False