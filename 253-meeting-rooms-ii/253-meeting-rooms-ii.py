class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda a: a[0])
        n = len(intervals)
        
        rooms = [intervals[0][1]]
        for i in range(1, n):
            vis = False
            t = len(rooms)
            for r in range(t):
                if rooms[r] <= intervals[i][0]:
                    vis = True
                    rooms[r] = intervals[i][1]
                    break
            if not vis:
                rooms.append(intervals[i][1])
        return len(rooms)