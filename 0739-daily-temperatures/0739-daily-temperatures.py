class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        
        for i, curr in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)
        return answer