class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda a: a[0])
        rooms = []
        for s,e in intervals:
            add_new = True
            for i in range(len(rooms)):
                if s >= rooms[i]:
                    rooms[i] = e
                    add_new = False
                    break
            if add_new:
                rooms.append(e)
        return len(rooms)
                