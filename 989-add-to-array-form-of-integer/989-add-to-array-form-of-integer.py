class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = num[::-1]
        n = len(num)
        carry = k
        for i in range(n):
            if carry == 0:
                break
            temp = num[i] + carry
            num[i] = temp%10
            carry = temp//10
        if carry != 0:
            sCarry = str(carry)
            return [int(i) for i in sCarry] + num[::-1]
        else:
            return num[::-1]
            