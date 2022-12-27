class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        add = []
        n = len(capacity)
        for i in range(n):
            add.append(capacity[i] - rocks[i])
        add.sort()
        i = 0
        while i < n:
            if additionalRocks < add[i]:
                break
            additionalRocks -= add[i]
            i += 1
        return i