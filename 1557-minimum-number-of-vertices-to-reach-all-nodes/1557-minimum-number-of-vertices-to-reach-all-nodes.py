class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indeg = [0]*n
        
        globalVis = [False]*n
        
        for u,v in edges:
            g[u].append(v)
            indeg[v] += 1
            
        ll = []
        
        for i in range(n):
            if indeg[i] == 0:
                ll.append(i)
        return ll
            
#         def bfs(node):
#             vis = [False]*n
#             q = deque()
#             q.append(node)
#             vis[node] = True
#             if not globalVis[node]:
#                 globalVis[node] = True
#             while q:
#                 count = len(q)
#                 for _ in range(count):
#                     temp = q.popleft()
#                     for i in g[temp]:
#                         if not globalVis[i]:
#                             globalVis[i] = True
#                         if not vis[i]:
#                             vis[i] = True
#                             q.append(i)
         
#         ans = []
#         for i in ll:
#             bfs(i)
#             ans.append(i)
#             if sum(globalVis) == n:
#                 return ans