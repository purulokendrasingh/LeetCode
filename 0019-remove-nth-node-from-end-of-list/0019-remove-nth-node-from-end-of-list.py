# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head.next

        delay = n
        curr = head
        temp = head
        while temp.next:
            if delay > 0:
                delay -= 1
            else:
                curr = curr.next
            temp = temp.next
            
        if delay > 0:
            return head.next
            
        curr.next = curr.next.next
        return head