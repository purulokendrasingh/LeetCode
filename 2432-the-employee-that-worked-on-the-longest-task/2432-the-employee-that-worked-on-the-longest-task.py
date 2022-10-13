class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        log = [0]*(n)
        temp = 0
        for i in range(len(logs)):
            log[logs[i][0]] = max(log[logs[i][0]], logs[i][1]-temp)
            temp = logs[i][1]
        return log.index(max(log))