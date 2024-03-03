# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        l = 0
        temp = head
        while temp:
            l += 1
            temp = temp.next
            
        if l == n:
            return head.next
            
        l = l-n-1
        temp = head
        while l > 0:
            l -= 1
            temp = temp.next
        temp.next = temp.next.next
        return head