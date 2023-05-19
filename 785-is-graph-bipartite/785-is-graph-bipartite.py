class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        if n == 1:
            return True
        
        gc = [None]*n
        vis = [False]*n
        
        for i in range(n):
            if vis[i]:
                continue
        
            q = deque()
            q.append(i)
            vis[i] = True
            while q:
                count = len(q)
                for _ in range(count):
                    u = q.popleft()
                    cols = []
                    for v in graph[u]:
                        if gc[v] != None:
                            cols.append(gc[v])
                        if not vis[v]:
                            vis[v] = True
                            q.append(v)
                    col = 0
                    while col in cols:
                        col += 1
                    gc[u] = col

        return len(set(gc)) == 2