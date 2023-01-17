class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        ddict = {}
        ans = -1
        for i in range(n):
            if s[i] not in ddict:
                ddict[s[i]] = i
            else:
                ans = max(ans, i-ddict[s[i]]-1)
        return ans