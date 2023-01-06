class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        costs = list(accumulate(costs))
        if coins in costs:
            return costs.index(coins) + 1
        else:
            bisect.insort(costs, coins)
            return costs.index(coins)