1. NAIVE SOLUTION:
```
class Solution:
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
s = []
curr = head
while curr:
s.append(curr.val)
curr = curr.next
curr = head
while curr:
curr.val = s.pop()
curr = curr.next
return head
```
​
2. Optimized solution without recursion:
```
class Solution:
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
prev = None
curr = head
while curr != None:
temp = curr.next
curr.next = prev
prev = curr
curr = temp
return prev
```