class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(list)
        for u,v in zip(s1, s2):
            if v not in graph[u]:
                graph[u].append(v)
            if u not in graph[v]:
                graph[v].append(u)
        
        def bfs(node):
            vis = defaultdict(bool)
            q = deque()
            q.append(node)
            vis[node] = True
            ans = ord(node)
            while q:
                count = len(q)
                for i in range(count):
                    temp = q.popleft()
                    for j in graph[temp]:
                        if not vis[j]:
                            vis[j] = True
                            q.append(j)
                            if ord(j) < ans:
                                ans = ord(j)
            return ans
        
        res = []
        for i in baseStr:
            res.append(chr(bfs(i)))
        return ''.join(res)
                            