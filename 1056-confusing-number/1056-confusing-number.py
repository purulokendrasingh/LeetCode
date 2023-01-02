class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = list(str(n))
        invalid = ['2','3','4','5','7']
        for i in invalid:
            if i in s:
                return False
        r = []
        for i in s:
            if i == '6':
                r.append('9')
            elif i == '9':
                r.append('6')
            else:
                r.append(i)
        return s != r[::-1]