class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = defaultdict(lambda: None)
        
        def helper(i):
            if dp[i] is not None:
                return dp[i]
            elif i == '':
                dp[i] = True
            else:
                ans = False
                for word in wordDict:
                    if i.startswith(word) and helper(i[len(word):]):
                        ans = True
                        break
                dp[i] = ans
            return dp[i]
        
        return helper(s)