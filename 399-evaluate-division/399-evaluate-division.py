class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)

        for i in range(n):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))
            
        vertices = list(graph.keys())
            
        def bfs(sourceNode, targetNode):
            if sourceNode not in vertices or targetNode not in vertices:
                return -1
            
            vis = set()
            q = deque([(sourceNode, 1)])
            vis.add(sourceNode)
            while q:
                count = len(q)
                for _ in range(count):
                    u, mult = q.popleft()
                    if u == targetNode:
                        return mult
                    for v, edge in graph[u]:
                        if v not in vis:
                            vis.add(v)
                            q.append((v, mult*edge))
            return -1
        
        ans = []
        for s,t in queries:
            ans.append(bfs(s,t))
        return ans