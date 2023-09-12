class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        c = dict(sorted(c.items(), key=lambda item: -item[1]))
        s = set()
        ans = 0
        values = list(c.values())
        i = 0
        while i < len(values):
            if values[i] not in s or values[i] == 0:
                s.add(values[i])
                i += 1
            else:
                values[i] -= 1
                ans += 1
        return ans