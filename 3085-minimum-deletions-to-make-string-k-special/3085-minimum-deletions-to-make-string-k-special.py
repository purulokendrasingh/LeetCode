class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        c = [v for k,v in Counter(word).most_common()][::-1]
        n = len(c)
        ans = 100000
        for i in range(n):
            temp = sum(c[:i])
            for j in range(i+1, n):
                if c[j] - c[i] > k:
                    temp += (c[j]-c[i]-k)
            
            ans = min(ans, temp)
        return ans