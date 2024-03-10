# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        if not head:
            return "Tie"
        score = 0
        
        temp = head
        while temp:
            if temp.val - temp.next.val > 0:
                score += 1
            else:
                score -= 1
            temp = temp.next.next
            
        if score == 0:
            return "Tie"
        elif score > 0:
            return "Even"
        else:
            return "Odd"