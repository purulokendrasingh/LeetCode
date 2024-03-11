class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        q = deque()
        q.append([left, right])
        
        def getElem(idx: int):
            if idx < 0 or idx >= len(nums):
                return -float('inf')
            else:
                return nums[idx]
            
        while q:
            l,r = q.popleft()
            if l <= r:
                mid = (l+r)//2
                if nums[mid] > getElem(mid-1) and nums[mid] > getElem(mid+1):
                    return mid
                
                q.append([l, mid-1])
                q.append([mid+1, r])
        
        return -1