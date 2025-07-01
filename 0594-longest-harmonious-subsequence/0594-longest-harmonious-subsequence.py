class Solution:
    def findLHS(self, nums: List[int]) -> int:
        MaxE = 0
        hashmap = Counter(nums)
                
        for i in hashmap.keys():
            if i+1 in hashmap:
                MaxE = max(hashmap[i] + hashmap[i+1], MaxE)
        return MaxE