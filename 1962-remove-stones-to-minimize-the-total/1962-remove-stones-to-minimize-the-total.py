class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapq.heapify(piles)
        for i in range(k):
            temp = heapq.heappop(piles)
            temp //= 2
            heapq.heappush(piles, temp)
        return abs(sum(piles))