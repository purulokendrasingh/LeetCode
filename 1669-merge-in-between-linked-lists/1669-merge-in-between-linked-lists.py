# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next
        
        a_prev = None
        b_next = None
        idx = 0
        temp = list1
        while temp:
            if idx == a-1:
                a_prev = temp
            elif idx == b:
                b_next = temp.next
            temp = temp.next
            idx += 1
            
        if a_prev is not None:
            a_prev.next = list2
        if b_next is not None:
            list2_tail.next = b_next
            
        return list1