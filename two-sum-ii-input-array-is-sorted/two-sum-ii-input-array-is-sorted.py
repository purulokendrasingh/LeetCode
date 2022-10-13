class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(n)):
            temp = target - n[i]
            if n[i] in diff:
                return [diff[n[i]]+1, i+1]
            else:
                diff[temp] = i