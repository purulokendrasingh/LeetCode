class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        def helper(num):
            res = []
            idx = 1
            curr = num[0]
            cnt = 1
            while idx < len(num):
                if num[idx] == curr:
                    cnt += 1
                else:
                    res.append(str(cnt)+curr)
                    curr = num[idx]
                    cnt = 1
                idx += 1
            res.append(str(cnt)+curr)
            return ''.join(res)
        
        curr = '1'
        for _ in range(n-1):
            curr = helper(curr)
        return curr