class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        output = []
        acc = list(accumulate(sorted(nums)))
        length = len(nums)
        for q in queries:
            for i in range(length):
                if acc[i] > q:
                    output.append(i)
                    break
                elif i == length - 1:
                    output.append(length)
        return output