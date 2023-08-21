class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter, t_counter = defaultdict(int), defaultdict(int)
        
        for i, j in zip(s, t):
            s_counter[i] += 1
            t_counter[j] += 1
        
        return s_counter == t_counter