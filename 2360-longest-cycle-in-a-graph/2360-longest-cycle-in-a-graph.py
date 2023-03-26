class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        g =  defaultdict(lambda: -1)
        n = len(edges)
        vis = defaultdict(bool)
        
        for i in range(n):
            g[i] = edges[i]
            
        def helper(node):
            visited = {}
            med = -1
            flag = False
            temp = node
            index = 0
            while temp not in visited or not flag:
                if not vis[temp]:
                    vis[temp] = True
                    visited[temp] = index
                    if g[temp] != -1:
                        temp = g[temp]
                else:
                    flag = True
                    if temp in visited:
                        med = index - visited[temp]
                    else:
                        med = 1
                    break
                index += 1
                
            if med == 1:
                return -1
            return med
                
            # if visited.count(med) == 1:
            #     return -1
            # else:
            #     t = [i for i, j in enumerate(visited) if j == med]
            #     return t[1] - t[0]
            
        
        ans = -1
        for i in range(n):
            if not vis[i]:
                r = helper(i)
                if ans < r and r != 1:
                    ans = r
        return ans
                