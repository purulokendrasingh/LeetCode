class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        z = zip(profit, difficulty)
        z = sorted(z, key = lambda a: -a[0])
        ans = 0
        for w in worker:
            for i in z:
                if i[1] <= w:
                    ans += i[0]
                    break
        return ans