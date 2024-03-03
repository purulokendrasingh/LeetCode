# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        delay = n
        count = 0
        temp = head
        new_temp = head
        while temp:
            if delay >= 0:
                delay -= 1
            else:
                new_temp = new_temp.next
            temp = temp.next
            count += 1
            
        if count == n:
            return head.next
            
        new_temp.next = new_temp.next.next
        return head