class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        temp = None
        for i in intervals:
            if temp is None:
                temp = i
                continue
            
            if i[0] <= temp[1] and temp[1] < i[1]:
                temp[1] = i[1]
            elif i[0] > temp[1]:
                ans.append(temp)
                temp = i
        if temp is not None:
            ans.append(temp)
        return ans