# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        ans = None
        
        while head:
            if head not in nodes:
                nodes.append(head)
                head = head.next
            else:
                ans = head
                break
        
        return ans