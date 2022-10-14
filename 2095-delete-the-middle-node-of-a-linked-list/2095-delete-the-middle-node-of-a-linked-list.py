# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return None
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        k = n//2
        prev = None
        curr = head
        while k > 0:
            k -= 1
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head