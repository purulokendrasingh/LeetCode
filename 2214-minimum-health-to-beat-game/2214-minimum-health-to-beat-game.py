class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        minn = min(max(damage), armor)
        return sum(damage) + 1 - minn