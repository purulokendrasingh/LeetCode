class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        ans = []
        for k,v in c.most_common():
            ans.append(k*v)
        return ''.join(ans)