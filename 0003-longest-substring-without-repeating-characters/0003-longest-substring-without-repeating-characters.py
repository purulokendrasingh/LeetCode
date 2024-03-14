class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        d = {}
        curr = 0
        temp = 0
        while curr < n:
            if s[curr] not in d:
                d[s[curr]] = curr
                temp += 1
                curr += 1
            else:
                ans = max(ans, temp)
                curr = d[s[curr]]+1
                d = {}
                temp = 0
        return max(ans, temp)