class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = Counter(students)
        for i in sandwiches:
            if c[i] == 0:
                return sum(c.values())
            else:
                c[i] -= 1
        return 0