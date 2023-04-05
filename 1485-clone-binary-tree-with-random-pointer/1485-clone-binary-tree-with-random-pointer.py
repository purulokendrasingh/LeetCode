# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        nto = {}
        otn = {}
        random_mapping = {}
        
        def preorder(head):
            if head:
                if head.random:
                    random_mapping[head] = head.random
                preorder(head.left)
                preorder(head.right)
        
        preorder(root)
        
        def helper(rootOld):
            if rootOld:
                rootNew = NodeCopy(rootOld.val)
                nto[rootNew] = rootOld
                otn[rootOld] = rootNew
                rootNew.left = helper(rootOld.left)
                rootNew.right = helper(rootOld.right)
                return rootNew
            
        def preorderNew(head):
            if head:
                if nto[head] in random_mapping:
                    head.random = otn[random_mapping[nto[head]]]
                preorderNew(head.left)
                preorderNew(head.right)          
        
        ans = helper(root)
        preorderNew(ans)
        
        return ans
            
            