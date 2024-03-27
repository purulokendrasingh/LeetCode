# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        prev = None
        temp = head
        while temp:
            if temp.val not in s:
                s.add(temp.val)
                prev = temp
                temp = temp.next
                continue
                
            prev.next = temp.next
            temp = temp.next
            
        return head