class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = ['a','e','i','o','u']
        vc = [0]
        cnt = 0
        for i in s:
            if i in vowels:
                cnt += 1
            vc.append(cnt)
            
        print(vc)
        
        # if k == 1 and vc[-1] > 0:
        #     return 1
            
        ans = 0
            
        for i in range(n-k+1):
            ans = max(ans, vc[i+k] - vc[i])
            
        return ans
            