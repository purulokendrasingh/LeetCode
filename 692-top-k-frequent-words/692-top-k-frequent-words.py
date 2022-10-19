class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        c = sorted(c.items(), key = lambda a: (-a[1],a[0]))
        return [i[0] for i in c][:k]