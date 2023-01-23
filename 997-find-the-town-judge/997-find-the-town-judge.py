class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u,v in trust:
            graph[u].append(v)
        
        judge = -1
        for i in range(1,n+1):
            if not graph[i]:
                judge = i
        
        if judge == -1:
            return judge
        
        for i in range(1,n+1):
            if i != judge and judge not in graph[i]:
                return -1
            
        return judge
    
    