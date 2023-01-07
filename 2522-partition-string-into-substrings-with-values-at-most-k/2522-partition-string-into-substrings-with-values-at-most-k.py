class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans = 0
        l = [int(i) for i in s]
        temp = 0
        for i in l:
            if i > k:
                return -1
            ntemp = temp*10 + i
            if ntemp > k:
                temp = i
                ans += 1
            else:
                temp = ntemp
                
        if temp <= k:
            ans += 1
        else:
            return -1
        
        return ans