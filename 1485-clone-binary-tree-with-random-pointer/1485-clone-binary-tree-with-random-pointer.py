# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

import ctypes

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        otn = {}
        
        def preorder(head):
            node = None
            if head:
                if id(head) not in otn:
                    node = NodeCopy(head.val)
                    otn[id(head)] = id(node)
                else:
                    return ctypes.cast(otn[id(head)], ctypes.py_object).value
                node.random = preorder(head.random)
                node.left = preorder(head.left)
                node.right = preorder(head.right)
            return node
        
        ans = preorder(root)
        return ans      