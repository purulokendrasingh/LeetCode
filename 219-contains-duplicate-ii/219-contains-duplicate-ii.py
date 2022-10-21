class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = defaultdict(list)
        for i in range(len(nums)):
            a[nums[i]].append(i)
        for i in a.values():
            if len(i) == 1:
                continue
            for j in range(len(i)-1):
                if abs(i[j] - i[j+1]) <= k:
                    return True
        return False