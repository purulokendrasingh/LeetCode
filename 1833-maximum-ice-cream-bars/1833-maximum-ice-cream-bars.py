class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        costs = list(accumulate(costs))
        ans = 0
        if coins in costs:
            ans = costs.index(coins) + 1
        else:
            bisect.insort(costs, coins)
            ans = costs.index(coins)
        return ans