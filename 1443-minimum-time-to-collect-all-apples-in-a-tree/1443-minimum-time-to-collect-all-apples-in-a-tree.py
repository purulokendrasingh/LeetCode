class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        vis = [False]*n
        
        def dfs(n):
            nodes = graph[n]
            if all([vis[i] for i in nodes]):
                return 2 if hasApple[n] else 0
            ans = 0
            for node in nodes:
                if not vis[node]:
                    vis[node] = True
                    ans += dfs(node)
            if ans == 0:
                if hasApple[n]:
                    print(2, n)
                    return 2
                else:
                    print(ans, n)
                    return ans
            else:
                print(ans+2, n)
                return ans + 2
            
        vis[0] = True
        res = dfs(0)
        if res > 0:
            return res-2
        return 0