class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = defaultdict(list)
        for i in range(len(nums)):
            if a[nums[i]] and i - a[nums[i]][-1] <= k:
                return True
            a[nums[i]].append(i)
        return False