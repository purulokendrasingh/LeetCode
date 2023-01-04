class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks).values()
        if 1 in counts:
            return -1
        
        ans = 0
        for i in counts:
            div = i//3
            rem = i%3
            
            if rem == 0:
                ans += div
            elif rem == 1:
                ans += div + 1
            else:
                ans += div + 1
        return ans