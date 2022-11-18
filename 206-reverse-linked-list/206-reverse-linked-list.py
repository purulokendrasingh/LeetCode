# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution using recursion
        # For other approaches refer to notes
        if not head or not head.next:
            return head
        rest_head = self.reverseList(head.next)
        rest_tail = head.next
        rest_tail.next = head
        head.next = None
        return rest_head