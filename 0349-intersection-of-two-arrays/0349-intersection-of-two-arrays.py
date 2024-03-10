class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        for i in nums1:
            if i not in ans:
                ans[i] = False
                
        for i in nums2:
            if i in ans:
                ans[i] = True
        
        return [k for k,v in ans.items() if v]
            