"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)   
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        node = head
        while node:
            new_node = Node(node.val)
            new_node.next = node.next
            node.next = new_node
            node = node.next.next
            
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
            
        node = head.next
        while node and node.next:
            node.next = node.next.next
            node = node.next
        
        return head.next