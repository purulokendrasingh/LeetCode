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
​
3. Using recursion:
```
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
```