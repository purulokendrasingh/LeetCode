class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for idx, ticket in enumerate(tickets):
            diff = tickets[k]
            if idx > k:
                diff -= 1
            if ticket >= tickets[k]:
                ans += diff
            else:
                ans += ticket
        return ans