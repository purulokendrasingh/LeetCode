class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans = []
        s,l = newInterval
        prev = [-1,-1]
        isAdded = False
        for i in intervals:
            if s > i[1] or isAdded:
                ans.append(i)
                prev = i
                continue
            if i[0] <= s and i[1] >= s:
                s = i[0]
            elif s > prev[1] and i[0] > s:
                pass
            if i[0] <= l and i[1] >= l:
                l = i[1]
                ans.append([s,l])
                isAdded = True
            elif l > prev[1] and i[0] > l:
                ans.append([s,l])
                ans.append(i)
                isAdded = True
            prev = i
        if not isAdded:
            ans.append([s,l])
        return ans 