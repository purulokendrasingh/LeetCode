class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        vis = defaultdict(bool)
        
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
            
        def bfs(node):
            num = 1
            q = deque()
            q.append(node)
            vis[node] = True
            while q:
                count = len(q)
                for _ in range(count):
                    temp = q.popleft()
                    for v in g[temp]:
                        if not vis[v]:
                            num += 1
                            vis[v] = True
                            q.append(v)
            return num
        
        nodes = []
        for i in range(n):
            if not vis[i]:
                nodes.append(bfs(i))
        
        l = len(nodes)
        if l < 2:
            return 0
        
        acc = list(accumulate(nodes))
        ans = 0
        for i in range(l):
            ans += nodes[i]*(acc[l-1]-acc[i])
        return ans
        