# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        otn = {}
        
        def preorder(head):
            node = None
            if head:
                if head not in otn:
                    node = NodeCopy(head.val)
                    otn[head] = node
                else:
                    node = otn[head]
                    return node
                node.random = preorder(head.random)
                node.left = preorder(head.left)
                node.right = preorder(head.right)
            return node
        
        ans = preorder(root)
        return ans      