class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # APPROACH 1
        ans = []
        c = Counter(nums)
        c = sorted(c.items(), key = lambda a: -a[1])
        return [i[0] for i in c[:k]]
        