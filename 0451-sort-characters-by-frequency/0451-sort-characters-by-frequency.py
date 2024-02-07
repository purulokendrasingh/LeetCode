class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(int)
        for i in s:
            counter[i] += 1
        ans = []
        items = sorted(counter.items(), key = lambda x: -x[1])
        for k,v in items:
            ans.extend([k]*v)
        return ''.join(ans)