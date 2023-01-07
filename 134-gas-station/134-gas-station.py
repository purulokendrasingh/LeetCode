class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = 0
        curr = 0
        ss = 0
        for i in range(n):
            temp = gas[i] - cost[i]
            total += temp
            curr += temp
            if curr < 0:
                ss = i + 1
                curr = 0
        
        return ss if total >= 0 else -1