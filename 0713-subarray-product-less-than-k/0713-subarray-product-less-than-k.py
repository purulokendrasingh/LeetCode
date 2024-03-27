class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        temp = 1
        prod = [1]
        for i in nums:
            temp *= i
            prod.append(temp)
        
        ans = 0
        for i in nums:
            if i < k:
                ans += 1
        
        prev_r = None
        l,r = 1,1
        while l < len(prod):
            if r < len(prod) and prod[r]//prod[l-1] < k:
                r += 1
                continue
            else:
                if prev_r is None:
                    prev_r = r
                else:
                    if prev_r > l:
                        ans -= (prev_r - l)*(prev_r - l -1)//2
                    prev_r = r
                cnt = r-l
                if cnt > 1:
                    ans += cnt*(cnt-1)//2
                    
                if r == len(prod):
                    break
                    
                l = l+1
                r = l
        return ans 