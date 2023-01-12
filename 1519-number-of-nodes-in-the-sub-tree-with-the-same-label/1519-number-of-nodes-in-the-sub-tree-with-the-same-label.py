class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0]*n
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        vis = [False]*n
            
        def dfs(node):
            nbrs = graph[node]
            if all([vis[i] for i in nbrs]):
                ans[node] = 1
                return {labels[node]: ans[node]}
            dictt = {labels[node]: 1}
            for i in nbrs:
                if not vis[i]:
                    vis[i] = True
                    temp = dfs(i)
                    for k,v in temp.items():
                        if k in dictt:
                            dictt[k] += v
                        else:
                            dictt[k] = v
            ans[node] = dictt[labels[node]]
            return dictt
    
        vis[0] = True
        dfs(0)
        return ans          