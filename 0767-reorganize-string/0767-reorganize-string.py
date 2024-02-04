class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        c = Counter(s)
        
        if len(s) == 1:
            return s
        
        if len(c) < 2:
            return ''
        
        while c.most_common(1)[0][1] != 0:
            if not ans:
                char = c.most_common(1)[0][0]
                ans.append(char)
                c[char] -= 1
                continue
            
            mc = c.most_common(2)
            if mc[0][1] == 0:
                break
            if ans[-1] != mc[0][0]:
                ans.append(mc[0][0])
                c[mc[0][0]] -= 1
            elif ans[-1] != mc[1][0] and mc[1][1] > 0:
                ans.append(mc[1][0])
                c[mc[1][0]] -= 1
            else:
                break
                
        if len(ans) != len(s):
            return ""
        
        return "".join(ans)