# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        c = defaultdict(int)
        temp = head
        while temp:
            c[temp.val] += 1
            temp = temp.next
        
        temp = head
        prev = None
        for v in c.values():
            temp.val = v
            prev = temp
            temp = temp.next
            
        prev.next = None
        return head